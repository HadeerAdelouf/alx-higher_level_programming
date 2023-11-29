#!/usr/bin/python3
def magic_string(counter=[-1]):
    counter[0] += 1
    return "BestSchool" + ", BestSchool" * counter[0]
