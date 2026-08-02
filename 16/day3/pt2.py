from pathlib import Path

with Path("input.txt").open() as f:
    triangles = [list(map(int, sides.split())) for sides in f.read().splitlines()]

new_traingles = []
for i in range(0, len(triangles), 3):
    new_traingles.append([triangles[i][0], triangles[i + 1][0], triangles[i + 2][0]])
    new_traingles.append([triangles[i][1], triangles[i + 1][1], triangles[i + 2][1]])
    new_traingles.append([triangles[i][2], triangles[i + 1][2], triangles[i + 2][2]])

num_possible = 0
for side1, side2, side3 in new_traingles:
    if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:
        num_possible += 1

print(num_possible)
