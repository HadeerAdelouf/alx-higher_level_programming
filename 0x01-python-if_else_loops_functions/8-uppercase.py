#!/usr/bin/python3
def uppercase(str):
    for i in str:
        number = ord(i)
        if number in range(97, 123):
            number = number - 32
        print("{:c}".format(number), end="")
    print("")
