#!/usr/bin/env python3
import argparse
import os


TIME_PUNCHER_DIR_NAME = '.time-puncher'


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
            save_times("Yo.txt")
        else:
            add_time(args.time)
    else:
        print("Invalid args")


def parse_args():
    parser = argparse.ArgumentParser(description="To add")

    parser.add_argument('-s, --save', dest='save', action='store_true')
    parser.add_argument('time', nargs='?')

    return parser.parse_args()


def verify_args(args):
    if not args.time and not args.save:
        return False

    return True  # TODO


def save_times(output_file):
    print("Saving file at {}".format(output_file))  # TODO


def add_time(time_to_add):
    print("Adding time: {}".format(time_to_add))  # TODO


if __name__ == '__main__':
    init()
    run()
