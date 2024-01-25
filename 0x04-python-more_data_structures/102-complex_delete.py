#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    new_dict = a_dictionary.copy()
    for key, dict_value in a_dictionary.items():
        if dict_value == value:
            del new_dict[key]
    a_dictionary.clear()
    a_dictionary.update(new_dict)
    return new_dict
