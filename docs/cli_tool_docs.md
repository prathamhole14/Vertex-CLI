# Vertex CLI

Vertex CLI is a powerful command-line tool that leverages Large Language Models (LLMs) to answer queries and debug faster. With just a few commands, you can set up and start using advanced features like querying LLMs and generating insights.

**Complete Documentation:** [Vertex CLI Docs](https://prathamhole14.github.io/vrtx/)

---

## Installation and Setup

Follow these steps to get started:

### Install Vertex-CLI

To install [`vrtx`](https://pypi.org/project/vrtx/), run:

```bash
pip install vrtx
```

Gemini is installed by default. Add a provider extra if you need one:

```bash
pip install "vrtx[openai]"
pip install "vrtx[anthropic]"
```

After installation, initialize the CLI configuration file:

```bash
vrtx --setup
```

This will create an empty `models_config.json` under `~/.config/ai_model_manager/`.

---

### Install the Editable Version (For Development)

If you want to modify or contribute to Vertex CLI, install it in **editable mode**:

1. **Clone the repository:**

   ```bash
   git clone https://github.com/prathamhole14/vrtx
   cd Vertex-CLI
   ```

2. **Install dependencies and set up the project:**

   ```bash
   pip install -e ".[openai,anthropic]"
   ```

3. **Initialize the CLI configuration:**

   ```bash
   vrtx --setup
   ```

---

## Configuration

You can configure the CLI to use a specific LLM model by adding or updating your API key:

```bash
vrtx config gemini-flash-latest YOUR_MODEL_API_KEY
```

Replace `gemini-flash-latest` with your preferred model name and `YOUR_MODEL_API_KEY` with your API key.

To list all configured models:

```bash
vrtx list
```

To remove a model:

```bash
vrtx remove gemini-flash-lite-latest
```

To select a model as the default:

```bash
vrtx select gemini-flash-latest
```

---

## Usage

Once installed and configured, you can start chatting or debugging commands:

### Quick Command Reference

* **Convert an array to a NumPy array**

  ```bash
  vrtx "how to convert an array into a NumPy array"
  ```

* **Manage API keys for models**

  * Add or update a model’s API key:

    ```bash
    vrtx config <model-name> <api-key>
    ```
  * Remove a model:

    ```bash
    vrtx remove <model-name>
    ```
  * List all saved models and their API keys:

    ```bash
    vrtx list
    ```
  * Select a model to use:

    ```bash
    vrtx select <model-name>
    ```
  * Show available commands/help:

    ```bash
    vrtx -h
    vrtx chat -h
    ```

### Debugging (Beta Feature)

* Debug the last 3 commands (default):

  ```bash
  vrtx debug
  ```

* Debug a specific number of recent commands (e.g., last 5):

  ```bash
  vrtx debug -n 5
  ```

* Add a custom message to explain your assumptions or observations:

  ```bash
  vrtx debug -n 5 -p "I think this issue might be related to environment variables"
  ```

---

🔗 **Complete CLI Documentation:** [CLI Commands](https://prathamhole14.github.io/vrtx/cli_tool_docs/)
