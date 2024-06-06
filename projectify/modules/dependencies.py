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
        result = subprocess.run(
            ["uv", "--version"],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        return result.returncode == 0
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False


def install_uv():
    """
    This function is used to install the 'uv' tool based on the operating system.

    If the operating system is Linux or macOS, it first checks if 'brew' is installed and uses it to install 'uv'.
    If 'brew' is not available, it falls back to using 'curl'.
    If the operating system is Windows, it sets the execution policy to RemoteSigned and installs 'uv' using PowerShell.
    If the operating system is not supported, it prints an error message and exits the program.

    After the installation, it adds the installation path to the system's PATH environment variable.
    """
    os_name = platform.system()
    if os_name == "Linux":
        print(Fore.YELLOW + "Installing uv with curl...")
        subprocess.run(
            ["curl", "-LsSf", "https://astral.sh/uv/install.sh | sh"], shell=True
        )
    elif os_name == "Darwin":  # macOS is 'Darwin'
        try:
            # Check if brew is installed
            subprocess.run(
                ["brew", "--version"],
                check=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
            )
            print(Fore.GREEN + "Brew is installed. Installing uv with brew...")
            subprocess.run(["brew", "install", "uv"], check=True)
        except subprocess.CalledProcessError:
            print(Fore.YELLOW + "Brew is not installed. Installing uv with curl...")
            subprocess.run(
                ["curl", "-LsSf", "https://astral.sh/uv/install.sh | sh"], shell=True
            )
    elif os_name == "Windows":
        try:
            print(
                Fore.YELLOW + "Setting PowerShell execution policy to RemoteSigned..."
            )
            subprocess.run(
                [
                    "powershell",
                    "-Command",
                    "Set-ExecutionPolicy RemoteSigned -Scope CurrentUser -Force",
                ],
                check=True,
            )
            print(Fore.GREEN + "Execution policy set. Installing uv with PowerShell...")
            subprocess.run(
                ["powershell", "-c", "irm https://astral.sh/uv/install.ps1 | iex"],
                check=True,
            )
        except subprocess.CalledProcessError:
            print(
                Fore.RED
                + "No se pudo configurar la política de ejecución de PowerShell. "
                "Por favor, configúrela manualmente y vuelva a intentar."
            )
            sys.exit(1)
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


def ensure_uv_installed():
    """
    Verify if iv is installed in your systems.
    """
    if not is_uv_installed():
        print(Fore.YELLOW + "uv no está instalado. Instalando uv...")
        install_uv()
        if not is_uv_installed():
            print(
                Fore.RED + "No se pudo instalar uv automáticamente. "
                "Por favor, instálelo manualmente y vuelva a intentar."
            )
            sys.exit(1)
        else:
            print(Fore.GREEN + "uv instalado correctamente.")
    else:
        print(Fore.GREEN + "uv ya está instalado.")


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


def check_and_install_dependencies():
    """
    This function checks if the required packages are installed and installs them if necessary.
    """
    required_packages = ["colorama", "art", "packaging"]
    for package in required_packages:
        try:
            __import__(package)
        except ImportError:
            print(
                Fore.YELLOW
                + f"El paquete '{package}' no está instalado. Instalándolo..."
            )
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])
