#!/usr/bin/env python3

import sys

text = sys.argv[1:]

if text  :
    print("NONE")

else :
    for new_text in text:
        print(new_text.lower())
