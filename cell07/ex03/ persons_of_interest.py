#!/usr/bin/env python3

def famous_births(historical_figures):
   
    sorted_figures = sorted(historical_figures.values(), key=lambda x: x["date_of_birth"])
    for figure in sorted_figures:
        print(f"{figure['name']} is a great scientist born in {figure['date_of_birth']}.")

women_scientists = {
    "ada": { "name": "Ada Lovelace", "date_of_birth": "1815" },
    "cecilia": { "name": "Cecila Payne", "date_of_birth": "1900" },
    "lise": { "name": "Lise Meitner", "date_of_birth": "1878" },
    "grace": { "name": "Grace Hopper", "date_of_birth": "1906" }
}

if __name__ == "__main__":
    famous_births(women_scientists)
