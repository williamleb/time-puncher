import sys


class _ConsoleColor:
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    END = '\033[0m'


def log_info(message):
    """
    :type message: str
    """
    print("{}{}{}".format(_ConsoleColor.GREEN, message, _ConsoleColor.END))


def log_err(message):
    """
    :type message: str
    """
    print("{}{}{}".format(_ConsoleColor.RED, message, _ConsoleColor.END), file=sys.stderr)


def log_warn(message):
    """
    :type message: str
    """
    print("{}{}{}".format(_ConsoleColor.YELLOW, message, _ConsoleColor.END), file=sys.stderr)
