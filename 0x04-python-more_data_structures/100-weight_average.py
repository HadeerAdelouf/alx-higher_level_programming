#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    score_num = 0
    sum_num = 0

    for tup in my_list:
        score_num += tup[0] * tup[1]
        sum_num += tup[1]

    return (score_num /sum_num)
