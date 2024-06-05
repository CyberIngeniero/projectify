from art import text2art
from colorama import Fore


def print_header():
    """
    This function prints a header using the text2art library.
    The header text is "CyberIngeniero" and it's printed in cyan color.
    """
    header = text2art("CyberIngeniero")
    print(Fore.CYAN + header)
