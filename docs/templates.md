# Projectify! Templates

**Projectify!** supports the use of YAML templates to customize the setup of your Python projects. This allows you to define reusable configurations that can be quickly applied when starting a new project.

## What are Templates?

Templates in **Projectify!** are predefined configurations that specify the structure, dependencies, and settings for a new project. By using templates, you can ensure consistency across your projects and save time on repetitive setup tasks.

## Creating a Template

Templates are written in YAML format and stored in the `templates` directory within your project or in a central repository for reuse across multiple projects.

### Example Template

Here’s an example of a simple YAML template:

```yaml
# Template Name: basic-python-project

# Project structure
structure:
  - src/
  - src/__init__.py
  - tests/
  - tests/__init__.py
  - README.md
  - setup.py

# Dependencies
dependencies:
  - colorama
  - pytest
  - ruff

# Optional: Define a Python version
python_version: "3.9"

# Optional: Initialize Git repository
git_init: true

# Optional: Add pre-commit hooks
pre_commit_hooks:
  - id: ruff
    name: Ruff Linter
    entry: ruff
    language: python
    files: \.py$
  - id: black
    name: Black Formatter
    entry: black
    language: python
    files: \.py$

# Dockerfile setup
dockerfile:
  from: python:3.9-slim
  workdir: /app
  copy:
    - requirements.txt .
  run: pip install --no-cache-dir -r requirements.txt
  cmd: python main.py

# Makefile setup
makefile:
  install:
    - pip install -r requirements.txt
  test:
    - pytest
  lint:
    - ruff .
```

## Template Breakdown

- **structure**: Specifies the directories and files to create in the new project.
- **dependencies**: Lists the Python packages to install in the virtual environment.
- **python_version**: Optionally sets the Python version for the virtual environment.
- **git_init**: If set to `true`, initializes a Git repository in the new project.
- **pre_commit_hooks**: Defines pre-commit hooks to automate code quality checks.
- **dockerfile**: Provides instructions for generating a `Dockerfile` in the project.
- **makefile**: Defines common `Makefile` commands for easy project management.

## Using a Template

To use a template with Projectify!, specify the template name during the project initialization:

```bash
projectify init --template basic-python-project
```

This command will create a new project using the basic-python template, generating the structure, installing dependencies, and setting up any other configurations defined in the template.

## Best Practices

- **Reuse Templates**: Store templates in a central repository or share them across teams to promote consistency.
- **Customize as Needed**: Modify templates to suit the specific needs of different projects or teams.
- **Document Templates**: Provide clear documentation for each template, so others can easily understand and use them.

## Sharing Templates

You can share your templates with others by publishing them in a central repository or including them in your project's repository. This allows you to collaborate with others and reuse configurations across different projects.

## Final Thoughts

Templates in Projectify! provide a powerful way to standardize and streamline the setup of Python projects. By defining reusable configurations, you can ensure that every project starts with the right structure, dependencies, and tools, saving time and reducing setup errors.
