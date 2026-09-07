"""
Regression tests for BaseLLMProvider.generate().

LangChain 1.x returns ``AIMessage.content`` as a list of content blocks. Returning
it unchanged made every successful generation crash downstream with
``AttributeError: 'list' object has no attribute 'strip'``.
"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from langchain_core.messages import AIMessage

from vrtx.models.base import ModelConfig
from vrtx.models.base_provider import BaseLLMProvider


class _StubProvider(BaseLLMProvider):
    """Provider backed by a canned message instead of a real API call."""

    def __init__(self, message):
        self._message = message
        super().__init__(ModelConfig("stub-model", "google", "test-key", 0.7))

    def _create_llm(self):
        return type("_FakeLLM", (), {"invoke": lambda _self, prompt: self._message})()

    def get_provider_name(self):
        return "Stub"


def generate_from(content):
    return _StubProvider(AIMessage(content=content)).generate("hi")


def test_generate_flattens_content_blocks():
    """The bug: block lists must come back as a strippable string."""
    result = generate_from([{"type": "text", "text": "  OK  "}])
    assert isinstance(result, str)
    assert result.strip() == "OK"


def test_generate_joins_multiple_blocks():
    assert generate_from(
        [{"type": "text", "text": "Hello "}, {"type": "text", "text": "world"}]
    ) == ("Hello world")


def test_generate_skips_non_text_blocks():
    """Thinking blocks must not leak into the rendered output."""
    content = [{"type": "thinking", "thinking": "hmm"}, {"type": "text", "text": "answer"}]
    assert generate_from(content) == "answer"


def test_generate_accepts_string_content():
    assert generate_from("plain") == "plain"


def test_generate_handles_empty_content():
    assert generate_from([]) == ""
