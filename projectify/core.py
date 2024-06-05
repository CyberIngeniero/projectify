import sys

from colorama import Fore, init

from projectify.modules import (
    get_installed_python_versions,
    print_header,
    setup_project,
)

init(autoreset=True)


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


def main():
    """The main function that runs the project setup script."""
    try:
        print_header()

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


if __name__ == "__main__":
    main()
