import platform
import re
import subprocess
import sys

from colorama import Fore
from packaging import version

from .dependencies import ensure_uv_installed


def get_installed_python_versions():
    """
    This function retrieves the installed Python versions on the system.

    Returns
    -------
    list
        A list of installed Python versions in descending order.
        Each version is a string in the format 'major.minor.patch'.
        If no Python versions are found, an empty list is returned.
    """
    versions = set()
    try:
        if platform.system() == "Windows":
            result = subprocess.run(
                ["py", "-0p"], stdout=subprocess.PIPE, stderr=subprocess.PIPE
            )
            output = result.stdout.decode("utf-8")
            matches = re.findall(r" -V:(\d+\.\d+)", output)
            versions.update(matches)
        else:
            possible_commands = ["python3", "python"]
            for cmd in possible_commands:
                result = subprocess.run(
                    [cmd, "--version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE
                )
                output = (
                    result.stdout.decode("utf-8").strip()
                    or result.stderr.decode("utf-8").strip()
                )
                match = re.search(r"(\d+\.\d+\.\d+)", output)
                if match:
                    versions.add(match.group(1))
    except FileNotFoundError:
        pass

    return sorted(versions, key=lambda v: version.parse(v), reverse=True)


def create_virtual_environment(project_name, python_version):
    """
    This function sets up a virtual environment for a project with a specified Python version.

    Parameters
    ----------
    project_name : str
        The name of the project.
    python_version : str
        The desired Python version for the virtual environment.
    """
    # check if uv is installed
    ensure_uv_installed()

    result = subprocess.run(
        ["uv", "venv", f"--python=python{python_version}"],
        cwd=project_name,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    if result.returncode != 0:
        print(
            Fore.RED
            + f"No se encontró el intérprete para Python {python_version}. Intentando encontrar la versión más cercana disponible..."
        )
        closest_version = find_closest_python_version(python_version)
        if closest_version:
            print(Fore.YELLOW + f"Utilizando Python {closest_version} en su lugar.")
            subprocess.run(
                ["uv", "venv", f"--python=python{closest_version}"], cwd=project_name
            )
        else:
            print(
                Fore.RED
                + "No se pudo encontrar una versión de Python cercana. Por favor, elija otra versión."
            )
            sys.exit(1)


def find_closest_python_version(target_version):
    """
    This function finds the closest installed Python version to the target version.

    Parameters
    ----------
    target_version : str
        The target Python version to compare with the installed versions.
        This should be a string in the format of 'major.minor.patch'.

    Returns
    -------
    str
        The closest installed Python version to the target version.
        This is also a string in the format of 'major.minor.patch'.
    """
    available_versions = get_installed_python_versions()
    target_version = version.parse(target_version)
    closest_version = None
    smallest_diff = None
    for v in available_versions:
        v_parsed = version.parse(v)
        diff = abs(target_version - v_parsed)
        if smallest_diff is None or diff < smallest_diff:
            smallest_diff = diff
            closest_version = v
    return closest_version
