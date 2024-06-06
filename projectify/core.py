import argparse
import importlib.metadata
import os
import platform
import shutil
import subprocess
import sys

from colorama import Fore

from projectify.modules import (
    check_and_install_dependencies,
    get_installed_python_versions,
    print_header,
    setup_project,
)


def get_int_input(prompt, min_val, max_val):
    """Prompt the user for an integer input within a specified range.

    Args:
    prompt (str): The message to display to the user when asking for input.
    min_val (int): The minimum acceptable value for the input.
    max_val (int): The maximum acceptable value for the input.

    Returns:
    int: The user's input, which is an integer within the specified range.
    """
    while True:
        try:
            value = int(input(prompt))
            if value < min_val or value > max_val:
                raise ValueError
            return value
        except ValueError:
            print(
                Fore.RED + f"Por favor, ingrese un número entre {min_val} y {max_val}."
            )


def clean_project():
    """
    This function cleans the files and directories generated during the project setup process.
    It deletes the "dist", "build" directories and any directory that ends with ".egg-info".
    """
    print(Fore.CYAN + "Limpiando archivos generados...")
    folders_to_clean = ["dist", "build"]

    # Eliminar carpetas específicas
    for folder in folders_to_clean:
        if os.path.exists(folder):
            shutil.rmtree(folder)
            print(Fore.GREEN + f"Directorio '{folder}' eliminado exitosamente.")

    # Eliminar directorios que terminan en .egg-info
    for item in os.listdir("."):
        if item.endswith(".egg-info") and os.path.isdir(item):
            shutil.rmtree(item)
            print(Fore.GREEN + f"Directorio '{item}' eliminado exitosamente.")

    print(Fore.GREEN + "Archivos limpiados exitosamente.")


def install_dependencies():
    """
    This function installs the dependencies listed in the requirements.txt file
    using 'uv' inside a virtual environment if it exists.
    """
    print(Fore.CYAN + "Instalando dependencias...")

    venv_path = os.path.join(os.getcwd(), ".venv")
    if os.path.exists(venv_path):
        print(
            Fore.GREEN
            + "Entorno virtual encontrado. Instalando dependencias en el entorno virtual."
        )
        uv_executable = os.path.join(
            venv_path,
            "bin",
            "uv" if platform.system() != "Windows" else "Scripts\\uv.exe",
        )
        if os.path.exists(uv_executable):
            subprocess.check_call(
                [uv_executable, "pip", "install", "-r", "requirements.txt"]
            )
            print(Fore.GREEN + "Dependencias instaladas exitosamente.")
        else:
            print(
                Fore.RED + "No se encontró el ejecutable de 'uv' en el entorno virtual."
            )
            sys.exit(1)
    else:
        print(
            Fore.RED
            + "No se encontró un entorno virtual. Por favor, cree un entorno virtual primero."
        )
        sys.exit(1)


def run_tests():
    """
    This function runs the tests using 'pytest' if the 'tests' folder
    and the test configuration file exist.
    """
    print(Fore.CYAN + "Ejecutando pruebas...")

    tests_path = os.path.join(os.getcwd(), "tests")
    pytest_ini_path = os.path.join(os.getcwd(), "pytest.ini")

    if os.path.exists(tests_path) and os.path.isdir(tests_path):
        if os.path.exists(pytest_ini_path):
            subprocess.run(["pytest"])
            print(Fore.GREEN + "Pruebas ejecutadas exitosamente.")
        else:
            print(
                Fore.RED
                + "No se encontró el archivo de configuración de pruebas 'pytest.ini'."
            )
    else:
        print(Fore.RED + "No se encontró la carpeta 'tests'.")


def Init():
    """
    This function is the entry point for the project setup process.
    It prints the header, checks and installs dependencies, and then sets up
    the project based on user input.
    """
    try:
        # Print the header
        print_header()

        # check and install dependencies
        check_and_install_dependencies()

        project_name = input(Fore.CYAN + "Ingrese el nombre del proyecto: ")

        print(Fore.CYAN + "\nSeleccione su IDE:")
        print(Fore.CYAN + "1. VScode")
        print(Fore.CYAN + "2. Pycharm")
        print(Fore.CYAN + "3. Other")
        ide_choice = get_int_input(
            Fore.CYAN + "Ingrese la opción de su IDE favorito: ", 1, 3
        )

        installed_versions = get_installed_python_versions()
        if len(installed_versions) == 0:
            print(
                Fore.RED
                + "\nNo se encontró ninguna versión de Python instalada. Por favor, instale Python y vuelva a intentarlo."
            )
            sys.exit(1)
        elif len(installed_versions) == 1:
            python_version = installed_versions[0]
            print(
                Fore.YELLOW
                + f"\nSe encontró solo la versión de Python {python_version}. Creando venv con esta versión."
            )
        else:
            print(Fore.CYAN + "\nSeleccione la versión de Python:")
            for i, v in enumerate(installed_versions, 1):
                print(Fore.CYAN + f"{i}. Python {v}")
            version_choice = get_int_input(
                Fore.CYAN
                + "Ingrese la opción correspondiente a la versión de Python: ",
                1,
                len(installed_versions),
            )
            python_version = installed_versions[version_choice - 1]

        setup_project(project_name, python_version, ide_choice)
    except KeyboardInterrupt:
        print(Fore.RED + "\nProceso interrumpido por el usuario. Saliendo...")


def main():
    """
    The main function that runs the project setup script.
    """
    parser = argparse.ArgumentParser(
        description="Proyectify: Una herramienta para configurar estructuras de proyectos en Python"
    )
    parser.add_argument(
        "--version",
        "-v",
        action="version",
        version=f"Proyectify {importlib.metadata.version('projectify')}",
    )

    subparsers = parser.add_subparsers(dest="command")
    subparsers.add_parser("init", help="Crear un nuevo proyecto")
    subparsers.add_parser("clean", help="Limpiar archivos generados")
    subparsers.add_parser("install-dependencies", help="Instalar dependencias")
    subparsers.add_parser("run-tests", help="Ejecutar pruebas")
    subparsers.add_parser("lint", help="Ejecutar linter")
    subparsers.add_parser("format", help="Formatear código")
    subparsers.add_parser("generate-docs", help="Generar documentación")

    args = parser.parse_args()

    if args.command == "init":
        Init()
    elif args.command == "clean":
        clean_project()

    elif args.command == "install-dependencies":
        install_dependencies()

    elif args.command == "run-tests":
        run_tests()


if __name__ == "__main__":
    main()
