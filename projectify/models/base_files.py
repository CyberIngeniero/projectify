base_files = {
    "pyproject.toml": """[tool.ruff]
line-length = 88
indent-width = 4
include = ["pyproject.toml"]
extend-include = ["*.ipynb"]

[tool.ruff.lint]
select = ["E4", "E7", "E9", "F"]
ignore = [__init__.py]
fixable = ["ALL"]
unfixable = []
dummy-variable-rgx = "^(_+|(_+[a-zA-Z0-9_]*[a-zA-Z0-9]+?))$"

[tool.ruff.format]
quote-style = "single"
skip-magic-trailing-comma = false
line-ending = "auto"
docstring-code-format = true
docstring-code-line-length = "dynamic"
""",
    ".gitignore": """*.venv/
app/__pycache__/
modules/__pycache__/
utils/__pycache__/
notebooks/.ipynb_checkpoints/
data/
.vscode
.idea
""",
    "README.md": """# {project_name}
## Description

## Installation

## Usage

## Contributing

## License

## Contact

""",
    "Makefile": """SHELL := /bin/bash

# Determine the OS and set the activation command accordingly
ifeq ($(OS),Windows_NT)
    ACTIVATE = .venv\\Scripts\\activate
else
    ACTIVATE = source .venv/bin/activate
endif

.PHONY: activate install lint

activate: ## Activate the virtual environment
\t$(ACTIVATE)

install: activate ## Install the dependencies
\tuv pip install -r requirements.txt

lint: activate ## Run Ruff to lint the code
\truff .

docs: activate
\tmkdocs serve

generate-docs: activate
\tpython scripts/generate_docs.py
""",
    "app/main.py": """#! /usr/bin/env python
import os
import sys

if __name__ == "__main__":
    print("Hello, World!")
""",
    "modules/__init__.py": "",
    "utils/__init__.py": "",
    ".env": "",
    ".pre-commit-config.yaml": """repos:
  - repo: https://github.com/charliermarsh/ruff-pre-commit
    rev: v0.0.241
    hooks:
      - id: ruff
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v3.4.0
    hooks:
      - id: trailing-whitespace
      - id: end-of-file-fixer
      - id: check-yaml
      - id: check-json
""",
    "Dockerfile": """FROM python:{python_version}-slim
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "./app/main.py"]
""",
    ".dockerignore": """.venv
app/__pycache__/
modules/__pycache__/
utils/__pycache__/
notebooks/.ipynb_checkpoints/
.vscode
.idea
""",
    "mkdocs.yml": """site_name: {project_name} Documentation
nav:
  - Home: index.md
  - Notebooks: notebooks.md

plugins:
  - mkdocstrings

theme: readthedocs
""",
    "docs/index.md": """# Welcome to the documentation\n
## Getting Started
### Prerequisites
- Python 3.8 or higher

### Installation
1. Clone the repository
2. Create a virtual environment
3. Install the dependencies

### Usage
- Run the app
- Explore the notebooks
- Check the documentation
""",
    "scripts/generate_docs.py": """import os
def generate_docs_for_folder(folder_name):
    docs_folder = 'docs'
    folder_path = os.path.join(docs_folder, folder_name)
    os.makedirs(folder_path, exist_ok=True)

    # Listar archivos .py en la carpeta especificada
    folder_files = [f for f in os.listdir(folder_name) if f.endswith('.py') and not f.startswith('__')]

    # Crear el contenido del archivo .md
    content_lines = [f"# {folder_name.capitalize()} Documentation\n"]
    for file in folder_files:
        module_name = file.replace('.py', '')
        content_lines.append(f"::: {folder_name}.{module_name}\n")

    # Guardar el archivo .md en la carpeta de documentación
    md_file_path = os.path.join(docs_folder, f"{folder_name}.md")
    with open(md_file_path, 'w') as md_file:
        md_file.write('\\n'.join(content_lines))

if __name__ == "__main__":
    folders_to_process = ['modules', 'utils']
    for folder in folders_to_process:
        if os.path.exists(folder):
            generate_docs_for_folder(folder)
""",
    "requirements.txt": "",
    "pytest.ini": """[pytest]
testpaths =
    tests
addopts = -v -ra -q
log_cli=true
log_level=DEBUG
log_format = %(asctime)s %(levelname)s %(message)s
log_date_format = %Y-%m-%d %H:%M:%S
log_file = logs/pytest-logs.txt
log_file_level = INFO
filterwarnings = ignore
""",
    "tests/__init__.py": "",
    "tests/test.py": """# you can import your modules and test them here
import pytest

@pytest.fixture
def sample_data():
    return [1, 2, 3, 4]

def test_addition():
    assert 1 + 1 == 2

def test_subtraction():
    assert 2 - 1 == 1

def test_sum(sample_data):
    assert sum(sample_data) == 10

class TestMathOperations:
    def test_multiplication(self):
        assert 2 * 2 == 4

    def test_division(self):
        assert 4 / 2 == 2
""",
}
