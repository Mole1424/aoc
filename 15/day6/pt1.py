from pathlib import Path

with Path("input.txt").open() as f:
    instructions = f.read().splitlines()

grid = [[False] * 1000 for _ in range(1000)]

for instruction in instructions:
    command, top_corner, _, bottom_corner = instruction.removeprefix("turn ").split()

    start_x, start_y = tuple(map(int, top_corner.split(",")))
    end_x, end_y = tuple(map(int, bottom_corner.split(",")))

    for x in range(start_x, end_x + 1):
        for y in range(start_y, end_y + 1):
            if command == "on":
                grid[x][y] = True
            elif command == "off":
                grid[x][y] = False
            else:  # toggle
                grid[x][y] = not grid[x][y]

print(sum(sum(row) for row in grid))
