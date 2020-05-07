#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    different_elemen = set(set_1 ^ set_2)  # Craete a set with unique elements
    return different_elemen
