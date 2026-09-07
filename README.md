# vrtx

A modern CLI tool for interacting with multiple LLMs using LangChain.

## Features

- Unified interface for multiple LLM providers (Google Gemini, OpenAI, Anthropic Claude)
- Clean architecture following SOLID principles
- Conversation history management
- Shell command debugging
- Easy model switching

## Installation

```bash
pip install vrtx
```

Gemini works out of the box. OpenAI and Anthropic are optional extras, so their
packages are only downloaded if you ask for them:

```bash
pip install "vrtx[openai]"     # OpenAI models
pip install "vrtx[anthropic]"  # Anthropic Claude models
```

To work on Vertex-CLI itself, install from a clone instead:

```bash
git clone https://github.com/prathamhole14/vrtx.git
cd Vertex-CLI
pip install -e ".[openai,anthropic]"
```

## Quick Start

```bash
# Initialize configuration
vrtx --setup

# Configure a model (provider auto-detected from model name)
vrtx config gemini-3.6-flash YOUR_API_KEY
vrtx config gpt-4 YOUR_OPENAI_KEY
vrtx config claude-opus-5 YOUR_ANTHROPIC_KEY

# Or specify provider explicitly
vrtx config my-model YOUR_KEY --provider google

# Select active model
vrtx select gemini-3.6-flash

# Use it
vrtx "explain quantum computing"
```

## Commands

```bash
vrtx "your question"                  # Ask a question
vrtx chat <text>                      # Chat mode
vrtx debug                            # Debug shell commands
vrtx config <model> <api_key>         # Configure model (auto-detects provider)
vrtx config <model> <key> --provider <provider>  # Specify provider explicitly
vrtx list                             # List models
vrtx select <model>                   # Select active model
vrtx remove <model>                   # Remove model
```

## Supported Providers

- **Google Gemini**: `google` or `gemini` — installed by default
- **OpenAI**: `openai` — needs `pip install 'vrtx[openai]'`
- **Anthropic**: `anthropic` or `claude` — needs `pip install 'vrtx[anthropic]'`

## Configuration

Models are configured in `~/.config/ai_model_manager/models_config.json`

Example configuration:
```json
{
  "selected_model": "gemini-flash-latest",
  "models": {
    "gemini-flash-latest": {
      "provider": "google",
      "api_key": "your-api-key",
      "temperature": 0.7
    }
  }
}
```

## Documentation

- [Architecture](docs/ARCHITECTURE.md) - Technical architecture

## Requirements

- Python 3.10+
- LangChain and provider packages

---

## Usage

Once installed and configured, you can start chatting or debugging commands:

### Chat with the LLM

You can either use the `chat` subcommand or omit it entirely:

```bash
# Explicit subcommand
vrtx chat "Tell me about the solar system"

# Shortcut form (no subcommand)
vrtx "Tell me about the solar system"
```

Replace the quoted string with any query you'd like.

![alt text](docs/images/eg_matplotlib.gif)

🔗 **Complete CLI Documentation:** [CLI Commands](https://prathamhole14.github.io/vrtx/cli_tool_docs/)

---

## Debugging Mode (Beta Feature)

Debugging is currently in beta but can analyze recent shell commands to identify issues.

### Debug the Last 3 Commands (default)

```bash
vrtx debug
```

### Specify the Number of Commands to Debug

```bash
vrtx debug -n 5
```

### Add a Custom Debugging Message

```bash
vrtx debug -n 5 -p "Explain why \`git commit\` failed"
```

---

## Contributing

Contributions are welcome! Follow these steps to contribute:

1. **Fork the repository**
2. **Create a new branch**:

   ```bash
   git checkout -b feature/your-feature-name
   ```
3. **Commit your changes**:

   ```bash
   git commit -m "Add your feature description"
   ```
4. **Push your branch**:

   ```bash
   git push origin feature/your-feature-name
   ```
5. **Open a pull request**

🔗 **Contributor Guide:** [How to Contribute](https://prathamhole14.github.io/vrtx/contributors_guide/)

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

## Support

If you encounter any issues, open an issue on the **[GitHub repository](https://github.com/prathamhole14/vrtx/issues)**.
