import os

from src.utils.config import TIME_PUNCHER_DIR_NAME
from src.utils.errors import HourFormatError
from src.utils.log_utils import log_warn, log_err
from src.utils.time_utils import parse_time, format_time

_TIME_PUNCHER_CACHE_FILE_NAME = 'time-cache-lol'

_CACHE_PATH = os.path.join(os.environ['HOME'], TIME_PUNCHER_DIR_NAME, _TIME_PUNCHER_CACHE_FILE_NAME)


def read_cached_times():
    """
    :rtype: list of float
    """
    try:
        with open(_CACHE_PATH, 'r') as cache:
            try:
                times = [parse_time(time) for time in cache.readlines()]
            except HourFormatError:
                log_err("There was a problem while reading the time cache. Maybe it was modified by hand? Try deleting"
                        "the file {}.".format(_CACHE_PATH))
                return []

        return times
    except FileNotFoundError:
        return []


def write_times(times):
    """
    :type times: list of float
    """

    with open(_CACHE_PATH, 'w') as cache:
        cache.writelines(["{}\n".format(time) for time in sorted(times)])


def clear_cache():
    open(_CACHE_PATH, 'w').close()


def compute_total_time_in_cache():
    times = read_cached_times()

    working_time_spans = []
    while len(times) > 1:
        working_time_spans.append((times.pop(0), times.pop(0)))

    if len(times) == 1:
        log_warn("The time {} is not in pair and thus will be ignored.".format(format_time(times[0])))

    working_times = [time_ended_working - time_started_working
                     for time_started_working, time_ended_working in working_time_spans]

    return sum(working_times)
