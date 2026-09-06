import itertools
import sys
import time
import subprocess
from importlib.metadata import requires


def spin_loader(stop_event):
    """Display a spinning loader."""
    spinner = itertools.cycle(["-", "/", "|", "\\"])
    while not stop_event.is_set():
        sys.stdout.write(next(spinner))
        sys.stdout.flush()
        time.sleep(0.1)
        sys.stdout.write("\b")
    sys.stdout.write(" ")
    sys.stdout.flush()


def install_requirements():
    """Install the dependencies declared in pyproject.toml."""
    for package in requires("Vertex-CLI") or []:
        if "extra ==" not in package:  # skip optional [dev] extras
            subprocess.run([sys.executable, "-m", "pip", "install", package])


def prettify_llm_output(response):
    """Prettify LLM output using Rich markdown."""
    from rich.console import Console  # deferred, only needed to render a reply
    from rich.markdown import Markdown

    console = Console()
    md = Markdown(response.strip())
    console.print("\n", md, "\n")
