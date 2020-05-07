"""a function that tells me if a currenty thing is current

Checks the dates in the dict like thing that is passed to it to see if today
lies between the begin and the end date of that thing.

looks for begin_date and end_date and date-like things
"""
import datetime as dt

from regolith.dates import get_dates


def is_current(thing, now=None):
    """
    given a thing with dates, returns true if the thing is current

    looks for begin_ and end_ daty things (date, year, month, day), or just
    the daty things themselves. e.g., begin_date, end_month, month, and so on.

    Parameters
    ----------
    thing: dict
      the thing that we want to know whether or not it is current

    now: datetime.date object
      a date for now.  If it is None it uses the current date.  Default is None

    Returns
    -------
    bool

    """
    if not now:
        now = dt.date.today()
    dates = get_dates(thing)
    if not dates.get("end_date"):
        dates["end_date"] = dt.date(5000, 12, 31)
    current = False
    if dates.get("begin_date") <= now <= dates.get("end_date"):
        current = True
    return current
