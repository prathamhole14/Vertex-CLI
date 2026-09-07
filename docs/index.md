## Homepage

### Overview

**Vertex-CLI** is a command-line tool that lets you query Large Language Models (LLMs) and debug faster, straight from your terminal.

For example, you can run:

```bash
vrtx "tell me about the solar system"
```

![Example usage](images/eg_matplotlib.gif)

Replace `"tell me about the solar system"` with any query you like Vertex-CLI will generate a response using your selected LLM model.

---

### Installation

To install [`vrtx`](https://pypi.org/project/vrtx/), run:

```bash
pip install vrtx
```

Then initialize the CLI with:

```bash
vrtx --setup
```

---

###  Managing API Keys & Models

* **Add a model and its API key:**

  ```bash
  vrtx config <model-name> <api-key>
  ```

* **Remove a model:**

  ```bash
  vrtx remove <model-name>
  ```

* **List all configured models:**

  ```bash
  vrtx list
  ```

* **Select a model to use by default:**

  ```bash
  vrtx select <model-name>
  ```

---

### Documentation

* Full CLI tool docs: [CLI Tool Docs](cli_tool_docs.md)
* Contributor guide: [Contributors Guide](contributors_guide.md)
* API reference: [API Reference](references.md)
