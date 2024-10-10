#!/usr/bin/env python3

average = lambda scores: sum(scores.values()) / len(scores) if scores else 0

class_3B = {
    "marine": 18,
    "jean": 15,
    "coline": 8,
    "luc": 9
}

class_3C = {
    "quentin": 17,
    "julie": 15,
    "marc": 8,
    "stephanie": 13
}

if __name__ == "__main__":
    print(f"Average for class 3B: {average(class_3B):.2f}.")
    print(f"Average for class 3C: {average(class_3C):.2f}.")
