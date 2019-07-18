import argparse
import os

from src.punch import BACKUP_DIR
from src.utils.cache_utils import clear_cache, read_cached_times, compute_total_time_in_cache
from src.utils.time_utils import format_time


def run():
    _parse_args()

    save_times()


def _parse_args():
    parser = argparse.ArgumentParser(description="Saves the times stored for the day into a file.")

    return parser.parse_args()


def save_times():
    print("Saving file")

    with open(os.path.join(BACKUP_DIR, "file.txt"), 'w') as output:
        total_time = compute_total_time_in_cache()

        for time in read_cached_times():
            output.write("{}\n".format(format_time(time)))
        output.write("------------------------\n")
        output.write("Total time: {}".format(format_time(total_time)))

    clear_cache()

