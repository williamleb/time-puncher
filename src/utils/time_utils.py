from datetime import datetime

from src.utils.errors import HourFormatError

_MINUTES_TO_HOURS = 1 / 60
_HOURS_TO_MINUTES = 60

_HOUR_MIN_FORMAT = "%H:%M"


def parse_time(time_to_parse):
    """
    :type time_to_parse: str
    :rtype: float
    """
    try:
        # If the time is expressed as HH:MM
        hours, minutes = time_to_parse.split(':')
        return int(hours) + int(minutes) * _MINUTES_TO_HOURS
    except ValueError:
        try:
            # If the time is expressed as hours with a decimal value.
            return float(time_to_parse)
        except ValueError as e:
            raise HourFormatError(e)


def format_time(time_to_format):
    """
    :type time_to_format: float
    :rtype: str
    """
    hours = int(time_to_format)
    minutes = int((time_to_format - hours) * _HOURS_TO_MINUTES)

    return "{}:{}".format("{:02d}".format(hours), "{:02d}".format(minutes))


def get_current_time():
    """
    :rtype: str
    """

    return datetime.now().strftime(_HOUR_MIN_FORMAT)
