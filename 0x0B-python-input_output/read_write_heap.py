#!/usr/bin/python3
"""
Write a script that finds a string in the heap of a running process,
and replaces it.

    Read The /proc filesystem

    Usage: read_write_heap.py pid search_string replace_string
                where pid is the pid of the running process
                and strings are ASCII

    The script should look only in the heap of the process

    Output: you can print whatever you think is interesting

    On usage error, print an error message on stdout and exit with
    status code 1.
"""
from sys import argv, exit


def print_usage():
    """Print the usage string if script was used improperly"""

    usage = "Usage: \t$ {} <pid> <string to read> <string to write>"
    print(usage.format(argv[0]))
    exit(1)


def read_write_heap(pid, read_str, write_str):
    """replace read_str with write_str in proc with pid"""
    try:
        maps_file = open("/proc/{}/maps".format(pid), 'r')
    except IOError as e:
        print("Can't open file /proc/{}/maps: IOError: {}".format(pid, e))
        exit(1)
    heap_info = None
    for line in maps_file:
        if 'heap' in line:
            heap_info = line.split()
    maps_file.close()
    if 'heap' is None:
        print('No heap found!')
        exit(1)
    addr = heap_info[0].split('-')
    perms = heap_info[1]
    if 'r' not in perms or 'w' not in perms:
        print('Heap does not have read and/or write permission')
        exit(0)
    try:
        mem_file = open("/proc/{}/mem".format(pid), 'rb+')
    except IOError as e:
        print("Can't open file /proc/{}/maps: IOError: {}".format(pid, e))
        exit(1)
    heap_start = int(addr[0], 16)
    heap_end = int(addr[1], 16)
    mem_file.seek(heap_start)
    heap = mem_file.read(heap_end - heap_start)
    str_offset = heap.find(bytes(read_str, "ASCII"))
    if str_offset < 0:
        print("Can't find {} in /proc/{}/mem".format(read_str, pid))
        exit(1)
    mem_file.seek(heap_start + str_offset)
    mem_file.write(bytes(write_str + '\0', "ASCII"))

if (len(argv) == 4):
    pid = argv[1]
    search_str = argv[2]
    replace_str = argv[3]
    read_write_heap(pid, search_str, replace_str)
else:
    print_usage()
