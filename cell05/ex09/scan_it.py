#!/usr/bin/env python3
import sys
import re

if len(sys.argv) != 3:
    print("NONE")
else:
    first = sys.argv[1]
    second = sys.argv[2]
    all = re.findall(first,second)

    if all :
        print(len(all))
    else :
        print("NONE")