#!/usr/bin/env python3

find_the_redheads = lambda family: list(filter(lambda name: family[name] == "red", family.keys()))

dupont_family = {
    "florian": "red",
    "marie": "blond",
    "virginie": "brunette",
    "david": "red",
    "franck": "red"
}

if __name__ == "__main__":
    print(find_the_redheads(dupont_family))

