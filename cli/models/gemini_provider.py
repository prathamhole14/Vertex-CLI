"""Google Gemini provider implementation using LangChain."""

from __future__ import annotations

from typing import TYPE_CHECKING

from cli.models.base_provider import BaseLLMProvider

if TYPE_CHECKING:
    from langchain_core.language_models import BaseChatModel


class GeminiProvider(BaseLLMProvider):
    """Google Gemini LLM provider."""

    def _create_llm(self) -> BaseChatModel:
        # Deferred: importing this package costs ~780ms, so commands that never
        # talk to a model (list, config, select, --help) must not pay for it.
        from langchain_google_genai import ChatGoogleGenerativeAI

        kwargs = {
            "model": self.config.name,
            "google_api_key": self.config.api_key,
            "temperature": self.config.temperature,
        }
        if self.config.max_tokens:
            kwargs["max_output_tokens"] = self.config.max_tokens
        return ChatGoogleGenerativeAI(**kwargs)

    def get_provider_name(self) -> str:
        return "Google Gemini"
