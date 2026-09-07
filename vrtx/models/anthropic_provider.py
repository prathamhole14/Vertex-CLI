"""Anthropic Claude provider implementation using LangChain."""

from __future__ import annotations

from typing import TYPE_CHECKING
from vrtx.models.base_provider import BaseLLMProvider, load_backend

if TYPE_CHECKING:
    from langchain_core.language_models import BaseChatModel


class AnthropicProvider(BaseLLMProvider):
    """Anthropic Claude LLM provider."""

    def _create_llm(self) -> BaseChatModel:
        ChatAnthropic = load_backend("langchain_anthropic", "ChatAnthropic", "anthropic")
        kwargs = {
            "model": self.config.name,
            "anthropic_api_key": self.config.api_key,
            "temperature": self.config.temperature,
        }
        if self.config.max_tokens:
            kwargs["max_tokens"] = self.config.max_tokens
        return ChatAnthropic(**kwargs)

    def get_provider_name(self) -> str:
        return "Anthropic Claude"
