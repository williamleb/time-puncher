#!/usr/bin/env python3
import os
import pkgutil
import sys

import src.punch_modules
from src.utils.errors import RunNotImplementedError
from src.utils.log_utils import log_err

TIME_PUNCHER_DIR_NAME = '.time-puncher'
BACKUP_DIR_NAME = 'backups'

TIME_PUNCHER_DIR = os.path.join(os.environ['HOME'], TIME_PUNCHER_DIR_NAME)
BACKUP_DIR = os.path.join(TIME_PUNCHER_DIR, BACKUP_DIR_NAME)


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

    punch_modules = dict()
    try:
        punch_modules = get_all_punch_modules()
    except RunNotImplementedError:
        exit(1)

    if not verify_args(punch_modules):
        exit(1)

    punch_modules[sys.argv.pop(1)]()


def get_all_punch_modules():
    """
    :rtype: dict of (str, function)
    :raise RunNotImplementedError: Whenever a module that doesn't implement the function "run" is found in the
                                   package "punch_modules".
    """
    punch_modules = dict()

    try:

        for importer, punch_module_name, is_package in pkgutil.iter_modules(src.punch_modules.__path__):
            punch_module = importer.find_module(punch_module_name).load_module(punch_module_name)

            punch_modules[punch_module_name] = punch_module.run

    except AttributeError as e:
        log_err("A module for the punch command is not implemented correctly.")  # TODO: Better error message
        raise RunNotImplementedError(e)

    return punch_modules


def verify_args(punch_modules):
    """
    :type punch_modules: dict of (str, function)
    """
    if len(sys.argv) <= 1:
        log_err("TODO: Write this error (not enough args")  # TODO
        return False

    if sys.argv[1] not in punch_modules:
        log_err("TODO Not in blablabla")  # TODO
        return False

    return True


if __name__ == '__main__':
    init()
    run()
