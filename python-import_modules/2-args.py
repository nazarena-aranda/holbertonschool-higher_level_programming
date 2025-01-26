#!/usr/bin/python3
import sys

args_len = len(sys.argv) - 1

if args_len <= 1:
    print("{} argument:".format(args_len))
else:
    print("{} arguments:".format(args_len))

idx = 1
for arg in sys.argv[1:]:
    print("{}: {}". format(idx, arg))
    idx += 1
