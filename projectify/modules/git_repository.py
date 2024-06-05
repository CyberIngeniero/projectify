import subprocess


def initialize_git_repo(project_name):
    """Initialize a new Git repository in the specified project directory.

    Parameters
    ----------
    project_name : str
        The name of the project directory where the Git repository will be initialized.
    """
    subprocess.run(["git", "init"], cwd=project_name)
