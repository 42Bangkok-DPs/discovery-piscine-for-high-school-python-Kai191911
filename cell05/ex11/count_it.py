#!/usr/bin/env python3
import sys

word = sys.argv[1:]

if not word :
    print("NONE")
else :
    print(f"paramiter :{len(word)}")
    for words in word :
        print(f"{words} : {len(words)}")