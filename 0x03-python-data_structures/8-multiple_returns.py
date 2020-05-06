#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:
        lenght = len(sentence)
        first_letter = sentence[0:1]
        return lenght, first_letter
