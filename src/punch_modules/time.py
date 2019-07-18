import argparse

from src.utils.cache_utils import compute_total_time_in_cache
from src.utils.log_utils import log_info
from src.utils.time_utils import format_time


def run():
    _parse_args()

    _print_time()


def _parse_args():
    parser = argparse.ArgumentParser(description="Shows the currently saved times.")

    return parser.parse_args()


def _print_time():
    log_info("Current total time: {}".format(format_time(
        compute_total_time_in_cache(group_last_time_with_current_local_time=True)
    )))
