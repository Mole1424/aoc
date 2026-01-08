from pathlib import Path

with Path("input.txt").open() as f:
    rules, target = f.read().split("\n\n")
rules = list(tuple(line.split(" => ")) for line in rules.splitlines())
target = target.strip()

start = "e"
steps = 0
while target != start:
    for old, new in rules:
        current_pos = 0
        while True:
            current_pos = target.find(new, current_pos)
            if current_pos == -1:
                break
            target = target[:current_pos] + old + target[current_pos + len(new) :]
            steps += 1
            current_pos += 1
            if target == start:
                break
        if target == start:
            break
print(steps)
