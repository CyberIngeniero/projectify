import os
import platform
import sys

from colorama import Fore, Style

from .dependencies import (
    install_packages,
    install_tool,
    install_uv,
    is_tool_installed,
    is_uv_installed,
)
from .environment import create_virtual_environment
from .git_repository import initialize_git_repo
from .ide_configuration import create_ide_configuration
from .project_structure import create_project_structure


def separator():
    """
    The separator function prints a separator line to the console.
    """
    print(Fore.MAGENTA + "\n" + "=" * 80 + "\n")


def setup_project(project_name, python_version, ide_choice):
    """
    This function sets up a new Python project with the specified name, Python version, and IDE choice.
    It creates the project structure, installs necessary tools and packages, initializes a Git repository,
    sets up a virtual environment, and configures the selected IDE.

    Parameters
    ----------
    project_name : str
        The name of the project.
    python_version : str
        The version of Python to be used for the project.
    ide_choice : str
        The IDE to be used for the project.
    """
    # Creando estructura del proyecto
    if os.path.exists(project_name):
        print(
            Fore.RED
            + f"El directorio '{project_name}' ya existe. Por favor, elija otro nombre para el proyecto." + Style.RESET_ALL
        )
        sys.exit(1)

    separator()
    print(Fore.CYAN + "Creando estructura del proyecto..." + Style.RESET_ALL)
    create_project_structure(project_name, python_version)

    # Instalando uv
    separator()
    if not is_uv_installed():
        print(Fore.YELLOW + "uv no está instalado. Instalando uv..." + Style.RESET_ALL)
        install_uv()
    else:
        print(Fore.GREEN + "uv ya está instalado." + Style.RESET_ALL)

    # Instalando git
    separator()
    if not is_tool_installed("git"):
        print(Fore.YELLOW + "git no está instalado. Instalando git..." + Style.RESET_ALL)
        install_tool("git")
    else:
        print(Fore.GREEN + "git ya está instalado." + Style.RESET_ALL)

    # Instalando make
    separator()
    if platform.system() == "Windows":
        if not is_tool_installed("make"):
            print(Fore.RED + "make no está instalado." + Style.RESET_ALL)
            install_tool("make")
            if not is_tool_installed("make"):
                print(
                    Fore.YELLOW
                    + "Instálelo desde PowerShell con permisos de administrador: choco install make" + Style.RESET_ALL
                )
        else:
            print(Fore.GREEN + "make ya está instalado." + Style.RESET_ALL)
    else:
        if not is_tool_installed("make"):
            print(Fore.YELLOW + "make no está instalado. Instalando make..." + Style.RESET_ALL)
            install_tool("make")
        else:
            print(Fore.GREEN + "make ya está instalado." + Style.RESET_ALL)

    # Creando entorno virtual
    separator()
    print(Fore.CYAN + "Creando entorno virtual..." + Style.RESET_ALL)
    create_virtual_environment(project_name, python_version)

    # Inicializando repositorio Git
    separator()
    print(Fore.CYAN + "Inicializando repositorio Git..." + Style.RESET_ALL)
    initialize_git_repo(project_name)

    # Instalando dependencias
    separator()
    print(Fore.CYAN + "Instalando paquetes necesarios..." + Style.RESET_ALL)
    install_packages(
        project_name, ["ruff", "pre-commit", "mkdocs", "mkdocstrings", "pytest"]
    )

    # Configurando IDE
    separator()
    print(Fore.CYAN + "Configurando IDE seleccionado..." + Style.RESET_ALL)
    create_ide_configuration(project_name, ide_choice)

    # Mensaje final
    separator()
    print(Fore.CYAN + f"Proyecto {project_name} creado y configurado exitosamente." + Style.RESET_ALL)
