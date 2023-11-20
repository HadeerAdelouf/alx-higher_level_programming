#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    indexx = 0
    try:
        while indexx is not x:
            print(my_list[indexx], end='')
            indexx += 1
    except IndexError:
        None
    print()
    return indexx
