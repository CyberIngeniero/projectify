from art import text2art
from colorama import Fore, Style


def print_header():
    """
    This function prints a header using the text2art library.
    The header text is "Projectify!" and it's printed in cyan color.
    """
    header = text2art("Projectify!")
    byline = Fore.YELLOW + Style.BRIGHT + "by CyberIngeniero" + Style.RESET_ALL
    header_lines = header.split("\n")
    max_length = max(len(line) for line in header_lines)
    header_with_byline = [
        Fore.CYAN + line + " " * (max_length - len(line)) + byline if i == 0 else Fore.CYAN + line
        for i, line in enumerate(header_lines)
    ]
    print("\n".join(header_with_byline) + Style.RESET_ALL)
