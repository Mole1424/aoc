from pathlib import Path

with Path("input.txt").open() as f:
    wrapping_dimensions = [
        tuple(map(int, line.split("x"))) for line in f.read().splitlines()
    ]

total_length = 0
for l, w, h in wrapping_dimensions:
    total_length += 2 * min(l + w, l + h, h + w) + l * w * h

print(total_length)
