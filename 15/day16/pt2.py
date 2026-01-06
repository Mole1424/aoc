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
    all_match = True
    for key, value in aunt.items():
        if key in ["cats", "trees"]:
            if int(value) <= correct_values[key]:
                all_match = False
                break
        elif key in ["pomeranians", "goldfish"]:
            if int(value) >= correct_values[key]:
                all_match = False
                break
        elif correct_values[key] != int(value):
            all_match = False
            break
    if all_match:
        print(i)
        break
