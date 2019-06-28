import argparse

from src.utils.cache_utils import compute_total_time_in_cache
from src.utils.log_utils import log_info
from src.utils.time_utils import format_time


def run():
    args = _parse_args()

    if not _verify_args(args):
        exit(1)

    _print_time(args)


def _parse_args():
    parser = argparse.ArgumentParser(description="Shows the currently saved times.")

    return parser.parse_args()


def _verify_args(args):
    # TODO

    return True


def _print_time(args):
    log_info("Current total time: {}".format(format_time(compute_total_time_in_cache())))
