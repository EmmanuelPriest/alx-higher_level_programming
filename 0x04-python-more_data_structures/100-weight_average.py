#!/usr/bin/python3

def weight_average(my_list=[]):
    if not isinstance(my_list, list) or len(my_list) == 0:
        return 0

    average = 0
    score = 0
    for tpl in my_list:
        average += (tpl[0] * tpl[1])
        score += tpl[1]
    return average / score
