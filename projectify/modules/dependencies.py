import os
import platform
import subprocess
import sys

from colorama import Fore


def is_uv_installed():
    """
    Check if the 'uv' command line tool is installed on the system.

    This function tries to run the 'uv --version' command and checks if it
    executes successfully. If the command executes successfully, the function
    returns True, indicating that 'uv' is installed. If the command fails to
    execute, the function returns False, indicating that 'uv' is not installed.

    Returns
    -------
        bool
            True if 'uv' is installed, False otherwise.
    """
    try:
        subprocess.run(
            ["uv", "--version"],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        return True
    except subprocess.CalledProcessError:
        return False
    except FileNotFoundError:
        return False


def install_uv():
    """
    This function is used to install 'uv' tool based on the operating system.

    If the operating system is Linux or MacOS, it uses 'curl' to download and install 'uv' from the provided URL.
    If the operating system is Windows, it uses 'powershell' to download and install 'uv' from the provided URL.
    If the operating system is not supported, it prints an error message and exits the program.

    After the installation, it adds the installation path to the system's PATH environment variable.
    """
    os_name = platform.system()
    if os_name == "Linux" or os_name == "Darwin":  # macOS is 'Darwin'
        subprocess.run(
            ["curl", "-LsSf", "https://astral.sh/uv/install.sh", "|", "sh"], shell=True
        )
    elif os_name == "Windows":
        print(Fore.RED + "uv no está instalado. Instalando uv...")
        print(
            Fore.YELLOW
            + "PowerShell requiere una política de ejecución en [Unrestricted, RemoteSigned, ByPass] para ejecutar uv. Por ejemplo, para establecer la política de ejecución en 'RemoteSigned', ejecute:"
        )
        print(Fore.YELLOW + "Set-ExecutionPolicy RemoteSigned -scope CurrentUser")
        subprocess.run(
            ["powershell", "-c", "irm https://astral.sh/uv/install.ps1 | iex"],
            shell=True,
        )
    else:
        print(
            Fore.RED
            + f"Sistema operativo {os_name} no soportado para la instalación automática de uv."
        )
        sys.exit(1)
    # Añadir la ruta de instalación al PATH
    os.environ["PATH"] += os.pathsep + os.path.expanduser("~/.cargo/bin")


def is_tool_installed(tool):
    """
    Check if a given tool is installed on the system.

    This function attempts to run the tool with the '--version' argument. If the tool
    is installed and runs successfully, the function returns True. If the tool is not
    installed or if it fails to run, the function returns False.

    Parameters
    ----------
    tool : str
        The name of the tool to check.

    Returns
    -------
    bool
        True if the tool is installed, False otherwise.
    """
    try:
        subprocess.run(
            [tool, "--version"],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        return True
    except subprocess.CalledProcessError:
        return False
    except FileNotFoundError:
        return False


def install_tool(tool):
    """
    This function installs a specified tool on the system.

    The function first determines the operating system of the machine.
    If the OS is Linux, it uses the 'apt-get' command to install the tool.
    If the OS is macOS, it uses the 'brew' command to install the tool.
    If the OS is Windows, it also uses the 'brew' command to install the tool (assuming that Homebrew is installed on Windows).
    If the OS is not one of these three, it prints an error message and exits the program.

    After the installation, the function checks if the tool was installed successfully.
    If it was, it prints a success message. If it wasn't, it prints an error message.

    Parameters
    ----------
    tool : str
        The name of the tool to be installed.

    Returns
    -------
    None
    """
    os_name = platform.system()
    if os_name == "Linux":
        subprocess.run(["sudo", "apt-get", "install", "-y", tool])
    elif os_name == "Darwin":
        subprocess.run(["brew", "install", tool])
    elif os_name == "Windows":
        if tool == "make":
            print(Fore.RED + "make no está instalado.")
            print(
                Fore.YELLOW
                + "Instálelo desde PowerShell con permisos de administrador: choco install make"
            )
        else:
            print(Fore.RED + f"{tool} no está instalado.")
            print(
                Fore.YELLOW
                + f"Instálelo desde PowerShell con permisos de administrador: choco install {tool}"
            )
    else:
        print(
            Fore.RED
            + f"Sistema operativo {os_name} no soportado para la instalación automática de {tool}."
        )
        sys.exit(1)
    if is_tool_installed(tool):
        print(Fore.GREEN + f"{tool} instalado correctamente.")
    else:
        print(Fore.RED + f"Error al instalar {tool}. Por favor, instálelo manualmente.")


def install_packages(project_name, packages):
    """
    This function installs the specified packages for a given project.

    The function uses the subprocess module to run the pip install command for each package in the list.
    The command is run in the working directory specified by the project_name parameter.

    Parameters
    ----------
    project_name :str
        The name of the project. This is used as the working directory for the installation.
    packages : list
        A list of package names to be installed.

    Returns
    -------
    None
    """
    for package in packages:
        subprocess.run(["uv", "pip", "install", package], cwd=project_name)
