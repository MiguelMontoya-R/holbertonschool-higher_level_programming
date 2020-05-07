#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list.copy()
    for i in range(0, len(new_list)): # iterate in my_list copy
        if new_list[i] == search: # Find matches
            new_list[i] = replace # Replace the item
    return new_list
