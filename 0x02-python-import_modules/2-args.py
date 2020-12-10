#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv
    argc = len(argv)
    print("{} arguments{}".format(argc - 1, ":" if argc > 1 else "."))
    for i in range(1, argc):
        print("{}: {}".format(i, argv[i]))
