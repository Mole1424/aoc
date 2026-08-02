from pathlib import Path

with Path("input.txt").open() as f:
    numbers = f.read().splitlines()

keypad = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

current_position = [1, 1]
for number in numbers:
    for move in number:
        if move == "D":
            current_position[0] = min(current_position[0] + 1, 2)
        elif move == "U":
            current_position[0] = max(current_position[0] - 1, 0)
        elif move == "L":
            current_position[1] = max(current_position[1] - 1, 0)
        else:
            current_position[1] = min(current_position[1] + 1, 2)
    print(keypad[current_position[0]][current_position[1]], end="")
print("")  # force new line # noqa: FURB105
