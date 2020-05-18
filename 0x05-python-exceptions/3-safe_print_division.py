#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return
    finally:
        if b == 0:
            result = None
        print("Finally Result: {}".format(result))
