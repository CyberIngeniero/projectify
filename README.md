# 🤖📦 Proyectify: A Command-Line Tool for Quick Python Project Setup

Proyectify is a command-line tool that generates and sets up a Python project structure with all necessary configurations, including a virtual environment, IDE setup, Git integration, and documentation generation with MkDocs.

## Features

- Creation of the basic project structure with predefined folders.
- Configuration of base files such as pyproject.toml, .gitignore, Makefile, etc.
- Creation of a virtual environment with the specified Python version.
- Initialization of a Git repository.
- Installation of necessary packages such as ruff, pre-commit, mkdocs, mkdocstrings.
- Setup for popular IDEs (VScode, Pycharm).
- Automatic documentation generation for modules.

## Prerequisites

- Python 3.8 or higher.
- In macOS, DevsTools must be installed.

## Usage

### Running the package

To run the package and set up your project, use the following command:

```python
pip install projectify
```

### Interactive Options

During script execution, you will be prompted for the following options:

- **Project Name**: Enter the name of your new project.
- **IDE Selection**: Select your favorite IDE (VScode, Pycharm, Other).
- **Python Version**: Select the Python version to use. If only one version is installed, it will be used automatically.

## Dependency Installation

### Installing  `uv`

`uv` os installed automatically when running the package. If you want to install it manually, follow the instructions below.

#### macOS and Linux

```sh
curl -LsSf https://astral.sh/uv/install.sh | sh
```

#### Windows

```sh
irm https://astral.sh/uv/install.ps1 | iex
```

### Installing  `make` (only on Windows)

`make` is required to run the Makefile commands. To install `make` on Windows, use the following command:

```sh
choco install make
```

In Linux and macOS, `make` is installed by default.

## Project Structure

The package will generate the following folder structure:

```markdown
<project_name>/
│
├── app/
│   └── main.py
├── artifacts/
├── data/
├── docs/
│   └── index.md
├── images/
├── modules/
│   └── __init__.py
├── notebooks/
├── scripts/
│   └── generate_docs.py
├── utils/
│   └── __init__.py
├── .dockerignore
├── .env
├── .gitignore
├── .pre-commit-config.yaml
├── Dockerfile
├── Makefile
├── mkdocs.yml
├── pyproject.toml
└── README.md
```

## Documentation Generation

To generate and serve documentation with MkDocs, use the following commands:

```sh
make docs
```

To generate documentation for modules, run:

```sh
make generate-docs
```

## Configuration Details

`uv` for Virtual Environments

Proyectify uses uv, an extremely fast Python package installer and resolver written in Rust, as the virtual environment manager. For more information, refer to the [uv documentation](https://github.com/astral-sh/uv).

`ruff` for Linting and Formatting

Proyectify uses ruff as the linter and formatter. Ruff is An extremely fast Python linter and code formatter, written in Rust. For more information, refer to the [ruff documentation](https://github.com/astral-sh/ruff)

A base configuration is provided in the pyproject.toml file:

```toml
[tool.ruff]
line-length = 88
indent-width = 4
include = ["pyproject.toml", "src/**/*.py"]
extend-include = ["*.ipynb"]

[tool.ruff.lint]
select = ["E4", "E7", "E9", "F"]
ignore = []
fixable = ["ALL"]
unfixable = []
dummy-variable-rgx = "^(_+|(_+[a-zA-Z0-9_]*[a-zA-Z0-9]+?))$"

[tool.ruff.format]
quote-style = "single"
skip-magic-trailing-comma = false
line-ending = "auto"
docstring-code-format = true
docstring-code-line-length = "dynamic"
```

`mkdocs` for Documentation

Proyectify automates documentation generation using `mkdocs` and the `mkdocstrings` plugin to incorporate the docstrings of each module into the documentation. The `mkdocs.yml` configuration is provided to get you started:

```yaml
site_name: Project Documentation
nav:
  - Home: index.md
  - Notebooks: notebooks.md

plugins:
  - mkdocstrings

theme: readthedocs
```

## Scripts

`generate_docs.py`

This script traverses the `modules`  and `utils`  folders and creates `.md`  files in the docs directory with the documentation content of each module.

```python
import os

def generate_docs_for_folder(folder_name):
    docs_folder = 'docs'
    folder_path = os.path.join(docs_folder, folder_name)
    os.makedirs(folder_path, exist_ok=True)

    folder_files = [f for f in os.listdir(folder_name) if f.endswith('.py') and not f.startswith('__')]

    content_lines = [f"# {folder_name.capitalize()} Documentation\n"]
    for file in folder_files:
        module_name = file.replace('.py', '')
        content_lines.append(f"::: {folder_name}.{module_name}\n")

    md_file_path = os.path.join(docs_folder, f"{folder_name}.md")
    with open(md_file_path, 'w') as md_file:
        md_file.write('\n'.join(content_lines))

if __name__ == "__main__":
    folders_to_process = ['modules', 'utils']
    for folder in folders_to_process:
        if os.path.exists(folder):
            generate_docs_for_folder(folder)
```

This script is automatically executed when running the `make generate-docs` command. (Feel free to modify it according to your needs).

## Contribution

If you'd like to contribute to this project, you're welcome to submit a pull request or open an issue in the repository.

## License

This project is licensed under the MIT License. For more details, please refer to the LICENSE file.
