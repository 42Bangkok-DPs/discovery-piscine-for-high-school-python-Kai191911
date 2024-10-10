#!/usr/bin/env python3

import sys

def shrink(s): print(s[:8])
def enlarge(s): print(s + 'Z' * (8 - len(s)))

text = sys.argv[1:]

if not text:
    print("none")
else:
    for new_text in text:
        if len(new_text) > 8:
            shrink(new_text)
        elif len(new_text) < 8:
            enlarge(new_text)
        else:
            print(new_text)
