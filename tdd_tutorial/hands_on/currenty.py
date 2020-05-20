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
        print(i)

    return


def break_out_root_dicts_yaml(yaml_level):
    """

    Parameters
    ----------
    yaml_level

    Returns
    -------

    """
    rootdicts = []
    if type(yaml_level) == str or type(yaml_level) == int:
        return []
    elif type(yaml_level) == list:
        List_of_root_dicts = []
        for listPos in yaml_level:
            rootdicts = break_out_root_dicts_yaml(listPos)
            for dicts in rootdicts:
                List_of_root_dicts.append(dicts)
        return List_of_root_dicts
    elif type(yaml_level) == dict:
        List_of_root_dicts = []
        if len(break_out_root_dicts_yaml(yaml_level[list(yaml_level)[0]])) == 0:
            List_of_root_dicts.append(yaml_level)
        else:
            for key in yaml_level:
                rootdicts = break_out_root_dicts_yaml(yaml_level[key])
                for dicts in rootdicts:

                    List_of_root_dicts.append(dicts)
        return List_of_root_dicts

    return


if __name__ == "__main__":
    open_yaml_testing()
