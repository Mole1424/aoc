from pathlib import Path

with Path("input.txt").open() as f:
    numbers = f.read().splitlines()

keypad = [
    ["X", "X", "1", "X", "X"],
    ["X", "2", "3", "4", "X"],
    ["5", "6", "7", "8", "9"],
    ["X", "A", "B", "C", "X"],
    ["X", "X", "D", "X", "X"],
]

current_position = [2, 0]
for number in numbers:
    for move in number:
        previous_position = current_position.copy()
        if move == "D":
            current_position[0] = min(current_position[0] + 1, 4)
        elif move == "U":
            current_position[0] = max(current_position[0] - 1, 0)
        elif move == "L":
            current_position[1] = max(current_position[1] - 1, 0)
        else:
            current_position[1] = min(current_position[1] + 1, 4)

        if keypad[current_position[0]][current_position[1]] == "X":
            current_position = previous_position.copy()

    print(keypad[current_position[0]][current_position[1]], end="")
print("")  # force new line # noqa: FURB105
