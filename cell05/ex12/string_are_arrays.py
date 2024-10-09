#!/usr/bin/env python3
import sys

word = sys.argv[1:]

if len(sys.argv) != 2 :
    print("NONE")
else :
    x = sys.argv[1]
    y = x.count('z')

    if y == 0 :
        print("NONE")
    else :
        print("z" * y)