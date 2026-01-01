from pathlib import Path

with Path("input.txt").open() as f:
    line = f.readline().strip()

print(sum(1 if line[i] == "(" else -1 for i in range(len(line))))
