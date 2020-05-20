import pytest
import yaml
from tdd_tutorial.hands_on.currenty import break_out_root_dicts_yaml,is_current


@pytest.fixture()
def list_of_activityBollean_Tuples():
    with open("currenty_things.yml", 'r') as stream:
        data_loaded = yaml.safe_load(stream)
    list_of_root_strings = break_out_root_dicts_yaml(data_loaded)
#insert a way to append whether or not the dictionary is correct in a true/false
#manner

    return data_loaded

def test_is_current():
    for i in list_of_activityBollean_Tuples:
        is_current(list_of_activityBollean_Tuples(i))
