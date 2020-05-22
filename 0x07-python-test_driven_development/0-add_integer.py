#!/usr/bin/python3
def add_integer(a, b=98):
    if (a, b) != [int, float]:
        print("Must be a number")
    else:
        return (a + b)
