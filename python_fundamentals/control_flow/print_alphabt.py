#!/usr/bin/env python3
result = ""
for letter in range(ord("a"), ord("z") + 1):
    character = chr(letter)
    if character != "q" and character != "e":
        result += character
print("{}".format(result))
