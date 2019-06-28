import argparse
import os

from src.punch import BACKUP_DIR
from src.utils.cache_utils import clear_cache, read_cached_times, compute_total_time_in_cache
from src.utils.time_utils import format_time


def run():
    args = _parse_args()

    if not _verify_args(args):
        exit(1)

    save_times("Test")  # TODO Pass real arguments


def _parse_args():
    parser = argparse.ArgumentParser(description="Saves the times stored for the day into a file.")

    # TODO: Add parameters -> Output, Auto-Yes, Keep-Times

    parser.add_argument('-y, --yes', dest='yes', action='store_true',
                        help="Use this flag to skip verification (WIP/NotImplemented).")

    return parser.parse_args()


def _verify_args(args):
    # TODO

    return True


def save_times(output_file):
    print("Saving file at {}".format(output_file))  # TODO

    with open(os.path.join(BACKUP_DIR, "test.txt"), 'w') as output:
        total_time = compute_total_time_in_cache()

        for time in read_cached_times():
            output.write("{}\n".format(format_time(time)))
        output.write("------------------------\n")
        output.write("Total time: {}".format(format_time(total_time)))

    clear_cache()

