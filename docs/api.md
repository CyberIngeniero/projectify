# API Documentation

This section provides an overview of the main functions available in the `Projectify!` tool. Each function is explained with its purpose, parameters, and usage examples.

## Functions

### `get_int_input(prompt, min_val, max_val)`

**Description:**

Prompts the user for an integer input within a specified range.

**Parameters:**

- `prompt` (str): The message to display to the user when asking for input.
- `min_val` (int): The minimum acceptable value for the input.
- `max_val` (int): The maximum acceptable value for the input.

**Returns:**

- `int`: The user's input, which is an integer within the specified range.

**Example:**

```python
choice = get_int_input("Enter your choice: ", 1, 5)
```

---

### clean_project()

**Description:**

Cleans up generated directories such as dist, build, and *.egg-info.

**Usage:**

```python
clean_project()
```

---

### install_dependencies()

**Description:**

Installs the dependencies listed in the requirements.txt file using uv inside a virtual environment if it exists.

**Usage:**

```python
install_dependencies()
```

---

### run_tests()

**Description:**

Runs the tests using pytest if the tests folder and the test configuration file exist.

**Usage:**

```python
run_tests()
```

---

### run_linter()

**Description:**

Runs the ruff linter on the project codebase.

**Usage:**

```python
run_linter()
```

---

### format_code()

**Description:**

Formats the project codebase using ruff with the --fix option.

**Usage:**

```python
format_code()
```

---

### generate_docs()

**Description:**

Generates the project documentation using mkdocs.

**Usage:**

```python
generate_docs()
```

---

### Init()

**Description:**

This is the entry point for the project setup process. It prints the header, checks and installs dependencies, and then sets up the project based on user input.

**Usage:**

```python
Init()
```
