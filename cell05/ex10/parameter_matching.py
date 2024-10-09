#!/usr/bin/env python3
import sys

if len(sys.argv) != 2 :
    print("NONE")
else:
    word = sys.argv[1]
    que = input("What was the parameter? :")

    if word == que :
        print("GOOD JOB! ")
    else :
        print("Nope ,sorry....")
