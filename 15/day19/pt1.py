from pathlib import Path

with Path("input.txt").open() as f:
    rules, input = f.read().split("\n\n")
rules = list(tuple(line.split(" => ")) for line in rules.splitlines())
input = input.strip()

new_molecules = set()
print(rules)
for old, new in rules:
    current_pos = 0
    while True:
        current_pos = input.find(old, current_pos)
        if current_pos == -1:
            break
        new_molecules.add(input[:current_pos] + new + input[current_pos + len(old) :])
        current_pos += 1
print(len(new_molecules))
