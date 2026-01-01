from pathlib import Path

with Path("input.txt").open() as f:
    directions = list(f.readline().strip())

current_position = (0, 0)
visited = {current_position}
moves = {"<": (-1, 0), ">": (1, 0), "^": (0, 1), "v": (0, -1)}

for direction in directions:
    dx, dy = moves[direction]
    x, y = current_position
    current_position = (x + dx, y + dy)
    visited.add(current_position)

print(len(visited))
