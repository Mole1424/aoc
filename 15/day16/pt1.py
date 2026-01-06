from pathlib import Path

aunts = []
with Path("input.txt").open() as f:
    for line in f.read().splitlines():
        current_auntie = {}
        for value in line.split(": ", 1)[1].split(", "):
            key, val = value.split(": ")
            current_auntie[key] = val
        aunts.append(current_auntie)

correct_values = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1,
}

for i, aunt in enumerate(aunts, start=1):
    if all(
        key not in aunt or int(aunt[key]) == correct_values[key]
        for key in correct_values
    ):
        print(i)
        break
