import argparse

from src.utils.cache_utils import read_cached_times, write_times
from src.utils.errors import HourFormatError
from src.utils.log_utils import log_info, log_err
from src.utils.time_utils import parse_time


def run():
    args = _parse_args()

    if not _verify_args(args):
        exit(1)

    _add_time(args.time)


def _parse_args():
    parser = argparse.ArgumentParser(description="Adds a time for the day.")

    parser.add_argument('time',
                        help="Time to add for the day.")

    return parser.parse_args()


def _verify_args(args):
    # Verification 1: Time must be parsable (in a valid format).
    try:
        parse_time(args.time)
    except HourFormatError:
        log_err("")
        return False

    return True


def _add_time(time_to_add):
    """
    :type time_to_add: str
    """

    times = read_cached_times()
    times.append(parse_time(time_to_add))
    write_times(times)

    log_info("Added time {} to the cache.".format(time_to_add))
