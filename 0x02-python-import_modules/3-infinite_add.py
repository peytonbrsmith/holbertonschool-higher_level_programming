#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv
    argc = len(argv)
    value = 0
    for i in range(1, argc):
        value = value + (int(argv[i]))
    print(value)
