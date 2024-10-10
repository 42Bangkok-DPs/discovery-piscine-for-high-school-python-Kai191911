#!/usr/bin/env python3

array_of_names = lambda persons: [f"{first.capitalize()} {last.capitalize()}" for first, last in persons.items()]

persons = {
    "jean": "valjean",
    "grace": "hopper",
    "xavier": "niel",
    "fifi": "brindacier"
}

if __name__ == "__main__":
    print(array_of_names(persons))
