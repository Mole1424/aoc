from pathlib import Path

with Path("input.txt").open() as f:
    directions = list(f.readline().strip())

positions = [(0, 0), (0, 0)]  # [santa, robot]
visited = {positions[0]}

moves = {"<": (-1, 0), ">": (1, 0), "^": (0, 1), "v": (0, -1)}

for i, direction in enumerate(directions):
    dx, dy = moves[direction]
    x, y = positions[i % 2]
    positions[i % 2] = (x + dx, y + dy)
    visited.add(positions[i % 2])


print(len(visited))
