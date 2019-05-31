#!/usr/bin/env python3
import argparse
import os
import sys
import datetime
import pkgutil

import src.punch_modules
from src.utils.log_utils import log_info, log_err, log_warn


TIME_PUNCHER_DIR_NAME = '.time-puncher'
TIME_PUNCHER_CACHE_FILE_NAME = 'time-cache'
BACKUP_DIR_NAME = 'backups'

TIME_PUNCHER_DIR = os.path.join(os.environ['HOME'], TIME_PUNCHER_DIR_NAME)
CACHE_PATH = os.path.join(os.environ['HOME'], TIME_PUNCHER_DIR_NAME, TIME_PUNCHER_CACHE_FILE_NAME)
BACKUP_DIR = os.path.join(TIME_PUNCHER_DIR, BACKUP_DIR_NAME)

MINUTES_TO_HOURS = 1 / 60
HOURS_TO_MINUTES = 60


class HourFormatError(ValueError):
    pass


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

    if verify_args(args):
        if args.save:
            save_times("Yo.txt")  # TODO
        elif args.print:
            log_info("Current total time: {}".format(format_time(compute_total_time_in_cache())))
        else:
            add_time(args.time)
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


def add_time(time_to_add):
    """
    :type time_to_add: str
    """
    times = read_cached_times()
    with open(CACHE_PATH, 'w') as cache:
        times.append(parse_time(time_to_add))
        cache.writelines(["{}\n".format(time) for time in sorted(times)])

    log_info("Added time {} to the cache.".format(time_to_add))


def read_cached_times():
    try:
        with open(CACHE_PATH, 'r') as cache:
            times = [parse_time(time) for time in cache.readlines()]  # TODO Manage error

        return times
    except FileNotFoundError:
        return []


def parse_time(time_to_parse):
    """
    :type time_to_parse: str
    :rtype: float
    """
    try:
        # If the time is expressed as HH:MM
        hours, minutes = time_to_parse.split(':')
        return int(hours) + int(minutes) * MINUTES_TO_HOURS
    except ValueError:
        try:
            # If the time is expressed as hours with a decimal value.
            return float(time_to_parse)
        except ValueError as e:
            raise HourFormatError(e)


def format_time(time_to_format):
    """
    :type time_to_format: float
    :rtype: str
    """
    hours = int(time_to_format)
    minutes = int((time_to_format - hours) * HOURS_TO_MINUTES)

    return "{}:{}".format(hours, minutes)


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

    return punch_modules


def run():
    if not verify_args():
        exit(1)


def verify_args():
    if len(sys.argv) <= 1:
        log_err("TODO: Write this error")  # TODO
        return False

    # if


if __name__ == '__main__':
    init()
    get_all_punch_modules()
    # run_prev()
