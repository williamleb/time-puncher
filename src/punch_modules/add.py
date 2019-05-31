import argparse

from src.utils.cache_utils import CACHE_PATH, read_cached_times
from src.utils.log_utils import log_info
from src.utils.time_utils import parse_time


def run():
    args = _parse_args()

    # TODO Verify Args

    _add_time(args.time)


def _parse_args():
    parser = argparse.ArgumentParser(description="Adds a time to the cache.")  # TODO Better description

    parser.add_argument('time',
                        help="Time to add in cache.")

    return parser.parse_args()


def _verify_args(args):
    return True  # TODO


def _add_time(time_to_add):
    """
    :type time_to_add: str
    """
    times = read_cached_times()
    with open(CACHE_PATH, 'w') as cache:  # TODO Method in cache_util to write in cache
        times.append(parse_time(time_to_add))
        cache.writelines(["{}\n".format(time) for time in sorted(times)])

    log_info("Added time {} to the cache.".format(time_to_add))
