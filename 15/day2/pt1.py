from pathlib import Path

with Path("input.txt").open() as f:
    wrapping_dimensions = [
        tuple(map(int, line.split("x"))) for line in f.read().splitlines()
    ]

total_area = 0
for l, w, h in wrapping_dimensions:
    side1 = l * w
    side2 = w * h
    side3 = h * l

    total_area += 2 * side1 + 2 * side2 + 2 * side3 + min(side1, side2, side3)

print(total_area)
