import os

from projectify.models import vscode_files


def create_ide_configuration(project_name, ide_choice):
    """
    This function creates IDE configuration files for a project.

    Parameters
    ----------
    project_name : str
        The name of the project.
    ide_choice : int
        The choice of IDE. 1 for VS Code, 2 for PyCharm.
    """
    if ide_choice == 1:
        vscode_dir = os.path.join(project_name, ".vscode")
        os.makedirs(vscode_dir, exist_ok=True)

        # Creando archivos de configuración de VS Code
        for file, content in vscode_files.items():
            with open(os.path.join(vscode_dir, file), "w") as f:
                f.write(content)
    elif ide_choice == 2:
        os.makedirs(os.path.join(project_name, ".idea"), exist_ok=True)
