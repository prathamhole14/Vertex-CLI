"""
Tests for reading the current shell's history file.

`tex debug` used to read ~/.bash_history unconditionally, so it silently returned
nothing under zsh, and zsh's metafied bytes made a plain UTF-8 read raise
UnicodeDecodeError (which the old `except IOError` did not catch).
"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import pytest

from cli.chat_history import get_shell_history, history_file


@pytest.fixture
def histfile(tmp_path, monkeypatch):
    """Point HISTFILE at a scratch file."""
    path = tmp_path / "history"
    monkeypatch.setenv("HISTFILE", str(path))
    return path


def test_picks_zsh_history_under_zsh(monkeypatch):
    monkeypatch.delenv("HISTFILE", raising=False)
    monkeypatch.setenv("SHELL", "/usr/bin/zsh")
    assert history_file().endswith(".zsh_history")


def test_picks_bash_history_otherwise(monkeypatch):
    monkeypatch.delenv("HISTFILE", raising=False)
    monkeypatch.setenv("SHELL", "/bin/bash")
    assert history_file().endswith(".bash_history")


def test_strips_zsh_extended_history_prefix(histfile):
    histfile.write_text(": 1788704812:0;git status\n: 1788704877:0;ls -la\n")
    assert get_shell_history(2) == "git status\nls -la\n"


def test_reads_plain_bash_history(histfile):
    histfile.write_text("git status\nls -la\n")
    assert get_shell_history(2) == "git status\nls -la\n"


def test_returns_only_the_last_n_commands(histfile):
    histfile.write_text("".join(f": 1788704812:0;cmd{i}\n" for i in range(10)))
    assert get_shell_history(3) == "cmd7\ncmd8\ncmd9\n"


def test_joins_multiline_commands(histfile):
    histfile.write_text(": 1788704812:0;for i in 1 2\\\ndo echo $i\\\ndone\n")
    assert get_shell_history(1) == "for i in 1 2\ndo echo $i\ndone\n"


def test_survives_non_utf8_bytes(histfile):
    """zsh metafies non-ASCII bytes; a plain UTF-8 read raises UnicodeDecodeError."""
    histfile.write_bytes(b": 1788704812:0;echo caf\xb4\n: 1788704813:0;git log\n")
    assert get_shell_history(1) == "git log\n"


def test_missing_history_file_is_empty(tmp_path, monkeypatch):
    monkeypatch.setenv("HISTFILE", str(tmp_path / "absent"))
    assert get_shell_history(3) == ""
