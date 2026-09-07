# Vertex CLI

Vertex CLI is a powerful command-line tool that leverages Large Language Models (LLMs) to answer queries and debug faster. With just a few commands, you can set up and start using advanced features like querying LLMs and generating insights.

**Complete Documentation:** [Vertex CLI Docs](https://prathamhole14.github.io/Vertex-CLI/)

---

## Installation and Setup

Follow these steps to get started:

### Install Vertex-CLI

To install [`Vertex-CLI`](https://pypi.org/project/Vertex-CLI/), run:

```bash
pip install Vertex-CLI
```

Gemini is installed by default. Add a provider extra if you need one:

```bash
pip install "Vertex-CLI[openai]"
pip install "Vertex-CLI[anthropic]"
```

After installation, initialize the CLI configuration file:

```bash
vtx --setup
```

This will create an empty `models_config.json` under `~/.config/ai_model_manager/`.

---

### Install the Editable Version (For Development)

If you want to modify or contribute to Vertex CLI, install it in **editable mode**:

1. **Clone the repository:**

   ```bash
   git clone https://github.com/prathamhole14/Vertex-CLI
   cd Vertex-CLI
   ```

2. **Install dependencies and set up the project:**

   ```bash
   pip install -e ".[openai,anthropic]"
   ```

3. **Initialize the CLI configuration:**

   ```bash
   vtx --setup
   ```

---

## Configuration

You can configure the CLI to use a specific LLM model by adding or updating your API key:

```bash
vtx config gemini-flash-latest YOUR_MODEL_API_KEY
```

Replace `gemini-flash-latest` with your preferred model name and `YOUR_MODEL_API_KEY` with your API key.

To list all configured models:

```bash
vtx list
```

To remove a model:

```bash
vtx remove gemini-flash-lite-latest
```

To select a model as the default:

```bash
vtx select gemini-flash-latest
```

---

## Usage

Once installed and configured, you can start chatting or debugging commands:

### Quick Command Reference

* **Convert an array to a NumPy array**

  ```bash
  vtx "how to convert an array into a NumPy array"
  ```

* **Manage API keys for models**

  * Add or update a model’s API key:

    ```bash
    vtx config <model-name> <api-key>
    ```
  * Remove a model:

    ```bash
    vtx remove <model-name>
    ```
  * List all saved models and their API keys:

    ```bash
    vtx list
    ```
  * Select a model to use:

    ```bash
    vtx select <model-name>
    ```
  * Show available commands/help:

    ```bash
    vtx -h
    vtx chat -h
    ```

### Debugging (Beta Feature)

* Debug the last 3 commands (default):

  ```bash
  vtx debug
  ```

* Debug a specific number of recent commands (e.g., last 5):

  ```bash
  vtx debug -n 5
  ```

* Add a custom message to explain your assumptions or observations:

  ```bash
  vtx debug -n 5 -p "I think this issue might be related to environment variables"
  ```

---

🔗 **Complete CLI Documentation:** [CLI Commands](https://prathamhole14.github.io/Vertex-CLI/cli_tool_docs/)
