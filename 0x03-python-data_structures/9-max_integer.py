#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        my_max = my_list[0]
        for i in my_list:
            if my_max < i:
                my_max = i
        return my_max
