import pytest
import yaml
from tdd_tutorial.hands_on.currenty import is_current


@pytest.fixture()
def list_of_activityBollean_Tuples():
    with open("currenty_things.yml", 'r') as stream:
        data_loaded = yaml.safe_load(stream)
#insert a way to append whether or not the dictionary is correct in a true/false
#manner

    return data_loaded

def test_is_current():
    for i in list_of_activityBollean_Tuples:
        is_current(list_of_activityBollean_Tuples(i))
