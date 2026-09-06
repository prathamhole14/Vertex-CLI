"""Base provider implementation with common functionality."""

from importlib import import_module

from langchain_core.language_models import BaseChatModel
from cli.models.base import ILLMProvider, ModelConfig


def load_backend(module: str, name: str, extra: str):
    """Import an optional provider backend, or say how to install it."""
    try:
        return getattr(import_module(module), name)
    except ImportError:
        raise ImportError(
            f"Support for '{extra}' models is not installed. "
            f"Run: pip install 'Vertex-CLI[{extra}]'"
        ) from None


class BaseLLMProvider(ILLMProvider):
    """Base implementation for LLM providers."""

    def __init__(self, config: ModelConfig):
        self.config = config
        self.validate_config()
        self.llm: BaseChatModel = self._create_llm()

    def _create_llm(self) -> BaseChatModel:
        """Create LLM instance. Must be implemented by subclasses."""
        raise NotImplementedError("Subclasses must implement _create_llm")

    def generate(self, prompt: str, **kwargs) -> str:
        """Generate response from LLM."""
        if "temperature" in kwargs:
            self.llm.temperature = kwargs["temperature"]
        # LangChain 1.x returns content as a list of blocks; .text flattens it to a string.
        return self.llm.invoke(prompt).text

    def validate_config(self) -> bool:
        """Validate configuration."""
        if not self.config.api_key:
            raise ValueError(f"API key is required for {self.get_provider_name()}")
        if not self.config.name:
            raise ValueError("Model name is required")
        return True
