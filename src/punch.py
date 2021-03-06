#!/usr/bin/env python3
import os
import sys

from src.punch_modules import add
from src.utils.config import TIME_PUNCHER_DIR, BACKUP_DIR
from src.utils.errors import RunNotImplementedError, HourFormatError
from src.utils.log_utils import log_err
from src.utils.modules_utils import get_all_punch_modules
from src.utils.time_utils import parse_time, get_current_time


def init():
    make_time_puncher_dir()
    make_backup_dir()


def make_time_puncher_dir():
    if not os.path.exists(TIME_PUNCHER_DIR):
        os.mkdir(TIME_PUNCHER_DIR)


def make_backup_dir():
    if not os.path.exists(BACKUP_DIR):
        os.mkdir(BACKUP_DIR)


def run():
    # If no argument is given, we punch the current local time.
    if len(sys.argv) <= 1:
        sys.argv.append(get_current_time())
        add.run()
        exit(0)

    # If the first argument given is a time, we punch it.
    if _first_argument_is_time():
        add.run()
        exit(0)

    punch_modules = dict()
    try:
        punch_modules = get_all_punch_modules()
    except RunNotImplementedError:
        exit(1)

    if not _verify_args(punch_modules):
        exit(1)

    punch_modules[sys.argv.pop(1)]()


def _first_argument_is_time():
    """
    :rtype: bool
    """

    # If no argument is given, the first argument can't be a time.
    if len(sys.argv) <= 1:
        return False

    # If the time parsing works on the first argument, it means it's a time.
    try:
        parse_time(sys.argv[1])
    except HourFormatError:
        return False
    else:
        return True


def _verify_args(punch_modules):
    """
    :type punch_modules: dict of (str, function)
    """

    if len(sys.argv) <= 1:
        log_err("The 'punch' command takes at least one argument.")
        return False

    if sys.argv[1] not in punch_modules:
        log_err(
            "The punch module '{}' does not exist. Use 'punch modules' to get the list of all available "
            "modules.".format(sys.argv[1]))
        return False

    return True


if __name__ == '__main__':
    init()
    run()
