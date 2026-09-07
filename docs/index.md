## Homepage

### Overview

**Vertex-CLI** is a command-line tool that lets you query Large Language Models (LLMs) and debug faster, straight from your terminal.

For example, you can run:

```bash
vtx "tell me about the solar system"
```

![Example usage](images/eg_matplotlib.gif)

Replace `"tell me about the solar system"` with any query you like Vertex-CLI will generate a response using your selected LLM model.

---

### Installation

To install [`Vertex-CLI`](https://pypi.org/project/Vertex-CLI/), run:

```bash
pip install Vertex-CLI
```

Then initialize the CLI with:

```bash
vtx --setup
```

---

###  Managing API Keys & Models

* **Add a model and its API key:**

  ```bash
  vtx config <model-name> <api-key>
  ```

* **Remove a model:**

  ```bash
  vtx remove <model-name>
  ```

* **List all configured models:**

  ```bash
  vtx list
  ```

* **Select a model to use by default:**

  ```bash
  vtx select <model-name>
  ```

---

### Documentation

* Full CLI tool docs: [CLI Tool Docs](cli_tool_docs.md)
* Contributor guide: [Contributors Guide](contributors_guide.md)
* API reference: [API Reference](references.md)
