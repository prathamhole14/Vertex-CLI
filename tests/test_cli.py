"""
End-to-end tests for the `vtx` command line.

These drive `main()` as the console script does, with the provider factory stubbed
out, so the dispatch in cli/prompt.py and cli/llm.py runs without network access.
Everything below the CLI (ConfigurationManager, the factory) is covered elsewhere.
"""

import json
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import pytest

from cli import prompt
from cli.models.factory import LLMProviderFactory

pytestmark = pytest.mark.unit


@pytest.fixture
def cli(tmp_path, monkeypatch):
    """Run the CLI against a throwaway HOME with a stubbed LLM provider."""
    monkeypatch.setenv("HOME", str(tmp_path))
    monkeypatch.setenv("USERPROFILE", str(tmp_path))  # expanduser on Windows
    # HISTORY_FILE is resolved at import time, so HOME alone does not redirect it.
    monkeypatch.setattr(prompt, "HISTORY_FILE", str(tmp_path / "chat_history.json"))

    class _Stub:
        def generate(self, text, **kwargs):
            runner.prompts.append(text)
            return "stub answer"

    monkeypatch.setattr(LLMProviderFactory, "create", staticmethod(lambda config: _Stub()))

    def runner(*args):
        monkeypatch.setattr(sys, "argv", ["vtx", *args])
        prompt.main()

    runner.prompts = []
    runner.home = tmp_path
    runner.config = tmp_path / ".config" / "ai_model_manager" / "models_config.json"
    return runner


@pytest.fixture
def ready(cli):
    """A CLI with a model configured and selected."""
    cli("config", "gemini-flash-latest", "test-key")
    cli("select", "gemini-flash-latest")
    return cli


@pytest.mark.parametrize(
    "model, expected",
    [("gemini-flash-latest", "google"), ("gpt-4", "openai"), ("claude-opus-5", "anthropic")],
)
def test_config_auto_detects_provider(cli, model, expected):
    cli("config", model, "test-key")
    assert json.loads(cli.config.read_text())["models"][model]["provider"] == expected


def test_config_unknown_model_explains_how_to_fix(cli, capsys):
    cli("config", "my-model", "test-key")

    out = capsys.readouterr().out
    assert "Could not auto-detect provider" in out and "--provider" in out
    assert json.loads(cli.config.read_text())["models"] == {}


def test_list_marks_the_selected_model(ready, capsys):
    ready("list")

    out = capsys.readouterr().out
    assert "gemini-flash-latest [SELECTED]" in out
    assert "API Key: ✓" in out


@pytest.mark.parametrize("argv", [("what", "is", "2+2"), ("chat", "what", "is", "2+2")])
def test_chat_reaches_the_model(ready, capsys, argv):
    """Both the shortcut form and the explicit subcommand dispatch to the LLM."""
    capsys.readouterr()
    ready(*argv)

    assert "what is 2+2" in ready.prompts[0]
    assert "stub answer" in capsys.readouterr().out


def test_conversation_is_persisted(ready):
    ready("chat", "remember this")

    saved = json.loads((ready.home / "chat_history.json").read_text())
    assert [entry["role"] for entry in saved] == ["user", "assistant"]
    assert saved[1]["content"] == "stub answer"


def test_debug_forwards_recent_commands(ready, tmp_path, monkeypatch):
    histfile = tmp_path / "history"
    histfile.write_text(": 1788704812:0;git comit -m wip\n: 1788704813:0;pip instal requests\n")
    monkeypatch.setenv("HISTFILE", str(histfile))

    ready("debug", "-n", "2")

    sent = ready.prompts[0]
    assert "git comit -m wip" in sent and "pip instal requests" in sent
    assert ": 1788704812:0;" not in sent  # zsh prefix stripped


def test_failures_exit_with_a_message_not_a_traceback(cli, capsys):
    with pytest.raises(SystemExit) as excinfo:
        cli("hello")

    assert excinfo.value.code == 1
    err = capsys.readouterr().err
    assert err.startswith("Error: ") and "Traceback" not in err
