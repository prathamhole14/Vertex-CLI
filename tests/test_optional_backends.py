"""
OpenAI and Anthropic ship as extras, so their backends may not be installed.
Creating one without its package must explain the fix rather than raise a bare
ModuleNotFoundError.
"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import pytest

from cli.models import base_provider
from cli.models.base import ModelConfig
from cli.models.factory import LLMProviderFactory

pytestmark = pytest.mark.unit


@pytest.mark.parametrize(
    "model, provider, extra",
    [("gpt-4", "openai", "openai"), ("claude-opus-5", "anthropic", "anthropic")],
)
def test_missing_backend_names_the_extra_to_install(monkeypatch, model, provider, extra):
    def _missing(_name):
        raise ImportError("No module named 'langchain_x'")

    monkeypatch.setattr(base_provider, "import_module", _missing)

    with pytest.raises(ImportError, match=rf"pip install 'Vertex-CLI\[{extra}\]'"):
        LLMProviderFactory.create(ModelConfig(model, provider, "test-key", 0.7))


def test_gemini_needs_no_extra():
    """Gemini is a default dependency, so it must not go through load_backend."""
    provider = LLMProviderFactory.create(
        ModelConfig("gemini-flash-latest", "google", "test-key", 0.7)
    )
    assert provider.get_provider_name() == "Google Gemini"
