#!/usr/bin/env python3
import sys

if len(sys.argv) < 3:
    print("NONE")
else:
    for text in reversed(sys.argv[1:]):
        print(text)
