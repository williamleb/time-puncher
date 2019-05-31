#!/usr/bin/env python3
import argparse
import os
import sys
import datetime
import pkgutil

import src.punch_modules
from src.utils.errors import RunNotImplementedError
from src.utils.log_utils import log_info, log_err, log_warn
from src.utils.time_utils import format_time, parse_time

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


def run_prev():
    args = parse_args()

    if verify_args(dict()):
        if args.save:
            save_times("Yo.txt")  # TODO
        elif args.print:
            log_info("Current total time: {}".format(format_time(compute_total_time_in_cache())))
    else:
        print("Invalid args")


def parse_args():
    parser = argparse.ArgumentParser(description="To add")

    # TODO: Add parameters -> Output, Auto-Yes, Keep-Times
    parser.add_argument('-s, --save', dest='save', action='store_true',
                        help="Use this flag to save the currently stored times. It also erases every stored times.")

    parser.add_argument('-p, --print', dest='print', action='store_true',
                        help="Use this flag to print the current total time.")

    parser.add_argument('time', nargs='?',
                        help="Time to add in cache.")

    return parser.parse_args()


def save_times(output_file):
    print("Saving file at {}".format(output_file))  # TODO

    with open(os.path.join(BACKUP_DIR, "test.txt"), 'w') as output:
        total_time = compute_total_time_in_cache()

        for time in read_cached_times():
            output.write("{}\n".format(format_time(time)))
        output.write("------------------------\n")
        output.write("Total time: {}".format(format_time(total_time)))

    clear_cache()


def compute_total_time_in_cache():
    times = read_cached_times()

    working_time_spans = []
    while len(times) > 1:
        working_time_spans.append((times.pop(0), times.pop(0)))

    if len(times) == 1:
        log_warn("The time {} is not in pair and thus will be ignored.".format(format_time(times[0])))

    working_times = [time_ended_working - time_started_working
                     for time_started_working, time_ended_working in working_time_spans]

    return sum(working_times)


def clear_cache():
    open(CACHE_PATH, 'w').close()





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
