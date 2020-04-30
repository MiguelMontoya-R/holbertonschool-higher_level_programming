#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    n = len(sys.argv)
    add_result = 0
    for i in range(1, n):
        add_result += int(sys.argv[i])
    print("{:d}".format(add_result))
