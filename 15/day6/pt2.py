from pathlib import Path

with Path("input.txt").open() as f:
    instructions = f.read().splitlines()

grid = [[0] * 1000 for _ in range(1000)]

for instruction in instructions:
    command, top_corner, _, bottom_corner = instruction.removeprefix("turn ").split()

    start_x, start_y = tuple(map(int, top_corner.split(",")))
    end_x, end_y = tuple(map(int, bottom_corner.split(",")))

    for x in range(start_x, end_x + 1):
        for y in range(start_y, end_y + 1):
            if command == "on":
                grid[x][y] += 1
            elif command == "off":
                grid[x][y] = max(0, grid[x][y] - 1)
            else:  # toggle
                grid[x][y] += 2

print(sum(sum(row) for row in grid))
