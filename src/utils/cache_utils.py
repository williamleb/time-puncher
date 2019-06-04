import os

from src.punch import TIME_PUNCHER_DIR_NAME  # TODO Place that const in another file maybe
from src.utils.time_utils import parse_time

_TIME_PUNCHER_CACHE_FILE_NAME = 'time-cache-lol'

_CACHE_PATH = os.path.join(os.environ['HOME'], TIME_PUNCHER_DIR_NAME, _TIME_PUNCHER_CACHE_FILE_NAME)


def read_cached_times():
    """
    :rtype: list of float
    """
    try:
        with open(_CACHE_PATH, 'r') as cache:
            times = [parse_time(time) for time in cache.readlines()]  # TODO Manage error

        return times
    except FileNotFoundError:
        return []


def write_times(times):
    """
    :type times: list of float
    """

    with open(_CACHE_PATH, 'w') as cache:
        cache.writelines(["{}\n".format(time) for time in sorted(times)])

