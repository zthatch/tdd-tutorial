def is_current(activityDict):
    """
    Returns true if current and false if not.

    This function takes in a dictionary representing an activity and
    returns a boolean regarding whether or not that activity is currently
    ongoing.

    Parameters
    ----------
     activityDict: Dictionary
     Contains a dictionary of an activity that may or may not have a time period
     that may or may not be current.

    Returns
    -------

    """
    return False


import yaml


def open_yaml_testing():
    with open("currenty_things.yml", 'r') as stream:
        data_loaded = yaml.safe_load(stream)

    list_of_root_strings = break_out_root_dicts_yaml(data_loaded)
    for i in list_of_root_strings:
        print(list_of_root_strings[i])

    return


def break_out_root_dicts_yaml(yaml_level):
    """

    Parameters
    ----------
    yaml_level

    Returns
    -------

    """

    list_of_root_dicts = []
    for key in yaml_level:
        if type(yaml_level[key]) == str:
            print("key =" + key + "value = " + yaml_level[key])
            list_of_root_dicts.append(yaml_level)
        elif type(yaml_level[key]) == list:
            for listPos in yaml_level[key]:
                break_out_root_dicts_yaml(yaml_level[key][listPos])
        elif type(yaml_level[key]) == dict:
            break_out_root_dicts_yaml(yaml_level[key])

    return list_of_root_dicts


if __name__ == "__main__":
    open_yaml_testing()
