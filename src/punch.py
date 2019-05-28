#!/usr/bin/env python3
import argparse
import os
import datetime
from enum import Enum


TIME_PUNCHER_DIR_NAME = '.time-puncher'
TIME_PUNCHER_CACHE_FILE_NAME = 'time-cache'
BACKUP_DIR_NAME = 'backups'

TIME_PUNCHER_DIR = os.path.join(os.environ['HOME'], TIME_PUNCHER_DIR_NAME)
CACHE_PATH = os.path.join(os.environ['HOME'], TIME_PUNCHER_DIR_NAME, TIME_PUNCHER_CACHE_FILE_NAME)
BACKUP_DIR = os.path.join(TIME_PUNCHER_DIR, BACKUP_DIR_NAME)

MINUTES_TO_HOURS = 1 / 60
HOURS_TO_MINUTES = 60


class ConsoleColor:
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    END = '\033[0m'


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


def run():
    args = parse_args()

    if verify_args(args):
        if args.save:
            save_times("Yo.txt")  # TODO
        else:
            add_time(args.time)
    else:
        print("Invalid args")


def parse_args():
    parser = argparse.ArgumentParser(description="To add")

    # TODO: Add parameters -> Output, Auto-Yes, Keep-Times
    parser.add_argument('-s, --save', dest='save', action='store_true',
                        help="Use this flag to save the currently stored times. It also erases every stored times.")

    parser.add_argument('time', nargs='?',
                        help="Time to add in cache.")

    return parser.parse_args()


def verify_args(args):
    if not args.time and not args.save:
        return False

    return True  # TODO


def save_times(output_file):
    print("Saving file at {}".format(output_file))  # TODO

    times = read_cached_times()

    working_time_spans = []
    while len(times) > 1:
        working_time_spans.append((times.pop(0), times.pop(0)))

    if len(times) == 1:
        log_err("The time {} is not in pair and thus will be ignored.".format(times[0]))


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
    minutes = (time_to_format - hours) * HOURS_TO_MINUTES

    return "{}:{}".format(hours, minutes)


def log_info(str):
    """
    :type str: str
    """
    print("{}{}{}".format(ConsoleColor.GREEN, str, ConsoleColor.END))


def log_err(str):
    """
    :type str: str
    """
    print("{}{}{}".format(ConsoleColor.RED, str, ConsoleColor.END))


def log_warn(str):
    """
    :type str: str
    """
    print("{}{}{}".format(ConsoleColor.YELLOW, str, ConsoleColor.END))


if __name__ == '__main__':
    init()
    run()
