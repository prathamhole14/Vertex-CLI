import os
import json
import re

# zsh extended_history prefixes each entry with ": <start>:<elapsed>;".
ZSH_ENTRY = re.compile(r"^: \d+:\d+;")

DEFAULT_HISTORY_SIZE = 10


class ChatHistory:
    def __init__(self, path: str, max_length: int = DEFAULT_HISTORY_SIZE):
        self.path = path
        self.max_length = max_length
        self._ensure_file()
        self._load()

    def _ensure_file(self):
        parent = os.path.dirname(self.path)
        os.makedirs(parent, exist_ok=True)
        if not os.path.exists(self.path):
            with open(self.path, "w") as f:
                json.dump([], f)

    def _load(self):
        try:
            with open(self.path, "r") as f:
                self.history = json.load(f)
        except (json.JSONDecodeError, IOError):
            self.history = []

    def append(self, role: str, content: str):
        entry = {"role": role, "content": content}
        self.history.append(entry)
        self.history = self.history[-self.max_length :]
        self._save()

    def get_prompt(self) -> str:
        return "".join(f"{item['role'].capitalize()}: {item['content']}\n" for item in self.history)

    def _save(self):
        with open(self.path, "w") as f:
            json.dump(self.history, f, indent=2)


def history_file() -> str:
    """Path to the current shell's history file."""
    shell = os.path.basename(os.environ.get("SHELL", ""))
    default = "~/.zsh_history" if shell == "zsh" else "~/.bash_history"
    return os.path.expanduser(os.environ.get("HISTFILE") or default)


def get_shell_history(count: int) -> str:
    """Return the last `count` commands from the current shell's history file."""
    try:
        # zsh metafies non-ASCII bytes, so the file is not always valid UTF-8.
        with open(history_file(), errors="replace") as f:
            lines = f.read().splitlines()
    except OSError:
        return ""

    commands: list[str] = []
    for line in lines:
        if commands and commands[-1].endswith("\\"):
            # zsh stores a multi-line command as backslash-continued lines.
            commands[-1] = commands[-1][:-1] + "\n" + line
        else:
            commands.append(ZSH_ENTRY.sub("", line))
    return "".join(f"{command}\n" for command in commands[-count:])
