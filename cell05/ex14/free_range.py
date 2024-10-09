#!/usr/bin/env python3

import sys



if len(sys.argv) != 3 :
    print("NONE")
else :
    try :
        first = int(sys.argv[1])
        last = int(sys.argv[2])

        result = list(range(first,last + 1))

        print(result)

    except :
        print("NONE")