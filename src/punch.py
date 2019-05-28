#!/usr/bin/env python3
import argparse
import os


TIME_PUNCHER_DIR_NAME = '.time-puncher'

MINUTES_TO_HOURS = 1 / 60
HOURS_TO_MINUTES = 60


class HourFormatError(ValueError):
    pass


def init():
    make_time_puncher_dir()


def make_time_puncher_dir():
    time_puncher_dir = os.path.join(os.environ['HOME'], TIME_PUNCHER_DIR_NAME)

    if not os.path.exists(time_puncher_dir):
        os.mkdir(time_puncher_dir)


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

    parser.add_argument('time', nargs='?')

    return parser.parse_args()


def verify_args(args):
    if not args.time and not args.save:
        return False

    return True  # TODO


def save_times(output_file):
    print("Saving file at {}".format(output_file))  # TODO


def add_time(time_to_add):
    """
    :type time_to_add: str
    """

    print("Adding time: {}".format(parse_time(time_to_add)))  # TODO


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


if __name__ == '__main__':
    init()
    run()
