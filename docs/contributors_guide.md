# **Installing the Editable Version of Vertex-CLI**

## **1. Fork and Clone the Repository**
First, fork the repository on GitHub. Then, clone it to your local machine:

```bash
git clone https://github.com/[YourUserName]/vrtx
cd Vertex-CLI
```

## **2. Install in Editable Mode**
Run the following command to install the package in editable mode:

```bash
pip install -e .
```

This allows you to make changes to the code and use them immediately without reinstalling.

## **3. Initialize the CLI**
Run this command to set up the CLI and install necessary dependencies. It will add a free API key for you to get started:

```bash
vrtx-init
```

## **4. Configure the CLI with Your Model (Optional)**
If you have your own model API key, you can configure it like this:

```bash
vrtx config gemini-flash-latest <model-api-key>
```

Replace `gemini-flash-latest` with your model's name and `<model-api-key>` with your actual API key.

---
