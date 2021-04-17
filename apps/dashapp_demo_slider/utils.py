"""
Some functions referred frequently.
"""
from datetime import datetime

from apps.dashapp_demo_slider.constants import TIME_STR_FMT


def convert_str_2_timeobj(time_str: str):
    """
    Convert a time string :param time_str to a Python time object.
    """
    return datetime.strptime(time_str, TIME_STR_FMT)


def convert_timeobj_2_str(time_obj) -> str:
    """
    Convert a time object to the desired time string.
    """
    return datetime.strftime(time_obj, TIME_STR_FMT)
