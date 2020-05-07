import pytest
import datetime as dt

from tdd_tutorial.hands_on.is_current import is_current
now = dt.date(2019, 6, 15)

@pytest.mark.parametrize("input,expected",[
    ({"begin_date": '2020-01-01', "end_date": '2020-12-31'}, False),
    ({"begin_date": '2019-01-01', "end_date": '2020-12-31'}, True),
    ({"begin_date": '2019-01-01'}, True),
    ({"begin_year": 2018}, True),
    ({"begin_year": 2019}, True),
    ({"begin_year": 2020}, False),
    ({"begin_year": 2019, "begin_month": "Apr"}, True),
    ({"begin_year": 2019, "begin_month": "Jun"}, True),
    ({"begin_year": 2019, "begin_month": "Jul"}, False),
    ({"begin_year": 2019, "begin_month": "Jun", "begin_day": 14}, True),
    ({"begin_year": 2019, "begin_month": "Jun", "begin_day": 15}, True),
    ({"begin_year": 2019, "begin_month": "Jun", "begin_day": 16}, False),
    ({"year": 2018}, False),
    ({"year": 2019}, True),
    ({"year": 2020}, False),
    ({"year": 2019, "month": "Apr"}, False),
    ({"year": 2019, "month": "Jun"}, True),
    ({"year": 2019, "month": "Jul"}, False),
    ({"year": 2019, "month": "Jun", "day": 14}, False),
    ({"year": 2019, "month": "Jun", "day": 15}, True),
    ({"year": 2019, "month": "Jun", "day": 16}, False),
])
def test_is_current(input, expected, now=now):
    assert is_current(input, now=now) == expected