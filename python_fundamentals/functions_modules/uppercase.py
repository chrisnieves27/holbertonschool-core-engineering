#!/usr/bin/env python3


def uppercase(str):
    for c in str:
        number = ord(c)
        if 97 <= number <= 122:
            number -= 32
        print("{}".format(chr(number)), end="")
    print()
