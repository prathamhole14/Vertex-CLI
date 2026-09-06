"""
Live API tests.

Skipped unless VERTEX_CLI_TEST_API_KEY is set, so the default suite stays offline.
Run them with:

    VERTEX_CLI_TEST_API_KEY=<key> pytest -m integration

VERTEX_CLI_TEST_MODEL overrides the model; the provider is inferred from its name.
The variable is deliberately not named GOOGLE_API_KEY, because conftest strips the
provider key variables before every test.
"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import pytest

from cli.models.base import ModelConfig
from cli.models.factory import LLMProviderFactory

API_KEY_ENV = "VERTEX_CLI_TEST_API_KEY"
MODEL_ENV = "VERTEX_CLI_TEST_MODEL"
DEFAULT_MODEL = "gemini-flash-latest"

pytestmark = [
    pytest.mark.integration,
    pytest.mark.skipif(
        not os.environ.get(API_KEY_ENV),
        reason=f"set {API_KEY_ENV} to run live API tests",
    ),
]


@pytest.fixture
def provider():
    """A provider for the model under test, with the provider inferred by name."""
    model = os.environ.get(MODEL_ENV) or DEFAULT_MODEL
    return LLMProviderFactory.create(
        ModelConfig(model, "auto", os.environ[API_KEY_ENV], temperature=0.0)
    )


def test_live_generation_returns_usable_text(provider):
    """Guards the content-block regression against the real API, not a stub."""
    answer = provider.generate("What is 7 times 6? Reply with just the number.")

    assert isinstance(answer, str), f"expected str, got {type(answer).__name__}"
    assert "42" in answer
