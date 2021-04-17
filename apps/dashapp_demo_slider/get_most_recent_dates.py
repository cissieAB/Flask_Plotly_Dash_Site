"""
This file gets the most recent 7 dates whose data is released.

Currently the most recent date is a mock value. Replace it with true value in the future.
"""
from typing import List
from datetime import timedelta

from apps.dashapp_demo_slider.constants import TIME_STR_FMT, TRACE_DAYS
from apps.dashapp_demo_slider.utils import convert_str_2_timeobj, convert_timeobj_2_str

# TODO: replace it with true most recent date
MOCK_MOST_RECENT_DATE = "Apr-07-2021"    # a string follow the format defined by TIME_STR_FMT


def get_7_recent_dates(most_recent_date: str) -> List[str]:
    """
    Get the most recent 7 dates with a list of strings.
    The last string is the :param most_recent_date.
    """
    base_date_obj = convert_str_2_timeobj(most_recent_date)
    most_recent_7_dates = []
    for i in range(1 - TRACE_DAYS, 1):
        most_recent_7_dates.append(convert_timeobj_2_str(base_date_obj + timedelta(days=i)))
    return most_recent_7_dates


last_date = MOCK_MOST_RECENT_DATE
MOST_RECENT_SEVEN_DATES = get_7_recent_dates(last_date)

# print(MOST_RECENT_SEVEN_DATES) # for debug
