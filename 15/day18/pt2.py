# this is just connway's game of life

from pathlib import Path

light_grid = []
with Path("input.txt").open() as f:
    for line in f.read().splitlines():
        light_grid.append([c == "#" for c in line])

light_grid[0][0] = True
light_grid[0][-1] = True
light_grid[-1][0] = True
light_grid[-1][-1] = True

num_steps = 100
directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
for _ in range(num_steps):
    new_grid = [
        [False for _ in range(len(light_grid[0]))] for _ in range(len(light_grid))
    ]
    for x in range(len(light_grid)):
        for y in range(len(light_grid[0])):
            lit_neighbours = 0
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < len(light_grid) and 0 <= ny < len(light_grid[0]):
                    if light_grid[nx][ny]:
                        lit_neighbours += 1
            if light_grid[x][y]:
                new_grid[x][y] = lit_neighbours == 2 or lit_neighbours == 3
            else:
                new_grid[x][y] = lit_neighbours == 3
    light_grid = new_grid
    light_grid[0][0] = True
    light_grid[0][-1] = True
    light_grid[-1][0] = True
    light_grid[-1][-1] = True

print(sum(sum(light for light in row) for row in light_grid))
