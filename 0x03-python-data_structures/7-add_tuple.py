#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    A1 = tuple_a[0] if len(tuple_a) > 0 else 0
    A2 = tuple_a[1] if len(tuple_a) > 1 else 0
    B1 = tuple_b[0] if len(tuple_b) > 0 else 0
    B2 = tuple_b[1] if len(tuple_b) > 1 else 0
    sum = ((A1 + B1), (A2 + B2))
    return (sum)
