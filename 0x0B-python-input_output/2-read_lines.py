#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):
    counter = 0
    if nb_lines <= 0:
        with open(filename, 'r') as f:
            for line in f:
                print(line, end="")
    else:
        with open(filename, 'r') as f:
            for line in f:
                if counter < nb_lines:
                    print(line, end="")
                    counter += 1
