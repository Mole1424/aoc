from pathlib import Path
import re

stats = []
with Path("input.txt").open() as f:
    for line in f:
        numbers = list(map(int, re.findall(r"-?\d+", line)))
        stats.append(numbers)

num_teaspoons = 100
num_calories = 500
max_score = 0

for num_item_1 in range(num_teaspoons + 1):
    for num_item_2 in range(num_teaspoons + 1 - num_item_1):
        for num_item_3 in range(num_teaspoons + 1 - num_item_1 - num_item_2):
            num_item_4 = num_teaspoons - num_item_1 - num_item_2 - num_item_3

            if (
                stats[0][4] * num_item_1
                + stats[1][4] * num_item_2
                + stats[2][4] * num_item_3
                + stats[3][4] * num_item_4
                != num_calories
            ):
                continue

            capacity = max(
                0,
                stats[0][0] * num_item_1
                + stats[1][0] * num_item_2
                + stats[2][0] * num_item_3
                + stats[3][0] * num_item_4,
            )
            durability = max(
                0,
                stats[0][1] * num_item_1
                + stats[1][1] * num_item_2
                + stats[2][1] * num_item_3
                + stats[3][1] * num_item_4,
            )
            flavor = max(
                0,
                stats[0][2] * num_item_1
                + stats[1][2] * num_item_2
                + stats[2][2] * num_item_3
                + stats[3][2] * num_item_4,
            )
            texture = max(
                0,
                stats[0][3] * num_item_1
                + stats[1][3] * num_item_2
                + stats[2][3] * num_item_3
                + stats[3][3] * num_item_4,
            )

            max_score = max(max_score, capacity * durability * flavor * texture)

print(max_score)
