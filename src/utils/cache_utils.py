import os

from src.punch import TIME_PUNCHER_DIR_NAME  # TODO Place that const in another file maybe
from src.utils.time_utils import parse_time

TIME_PUNCHER_CACHE_FILE_NAME = 'time-cache'

CACHE_PATH = os.path.join(os.environ['HOME'], TIME_PUNCHER_DIR_NAME, TIME_PUNCHER_CACHE_FILE_NAME)


def read_cached_times():
    try:
        with open(CACHE_PATH, 'r') as cache:
            times = [parse_time(time) for time in cache.readlines()]  # TODO Manage error

        return times
    except FileNotFoundError:
        return []