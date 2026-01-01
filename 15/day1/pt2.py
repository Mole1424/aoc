from pathlib import Path

with Path("input.txt").open() as f:
    line = f.readline().strip()

current_floor = 0

for i in range(len(line)):
    current_floor += 1 if line[i] == "(" else -1
    if current_floor == -1:
        print(i + 1)
        break
