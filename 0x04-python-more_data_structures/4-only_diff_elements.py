#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    new_set = set_1.copy()
    for i in set_2:
        if i in new_set:
            new_set.remove(i)
        else:
            new_set.add(i)
    return new_set
