from pathlib import Path

with Path("input.txt").open() as f:
    triangles = [list(map(int, sides.split())) for sides in f.read().splitlines()]

num_possible = 0
for side1, side2, side3 in triangles:
    if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:
        num_possible += 1

print(num_possible)
