import os

from projectify.models import base_files, directories


def create_project_structure(project_name, python_version):
    """
    This function creates a basic structure for a Python project.

    Parameters
    ----------
    project_name : str
        The name of the project. This will be used to create the main directory and replace placeholders in files.
    python_version : str
        The version of Python to be used in the project. This will be used to replace placeholders in the Dockerfile.
    """
    # Reemplazar variables en los archivos base
    base_files["README.md"] = base_files["README.md"].replace(
        "{project_name}", project_name
    )
    base_files["Dockerfile"] = base_files["Dockerfile"].replace(
        "{python_version}", python_version
    )
    base_files["mkdocs.yml"] = base_files["mkdocs.yml"].replace(
        "{project_name}", project_name
    )

    # Crear directorios base
    for directory in directories:
        os.makedirs(os.path.join(project_name, directory), exist_ok=True)

    for file, content in base_files.items():
        file_path = os.path.join(project_name, file)
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "w") as f:
            f.write(content)
