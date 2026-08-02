from pathlib import Path

with Path("input.txt").open() as f:
    moves = f.readline().strip().split(", ")

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
current_direction = 0
current_coords = [0, 0]

for move in moves:
    current_direction = (current_direction + (1 if move[0] == "R" else -1)) % 4
    current_coords[0] += directions[current_direction][0] * int(move[1:])
    current_coords[1] += directions[current_direction][1] * int(move[1:])

print(abs(current_coords[0]) + abs(current_coords[1]))
