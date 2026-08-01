from functools import reduce
from itertools import combinations
from pathlib import Path

with Path("input.txt").open() as f:
    weights = [int(weight) for weight in f.read().splitlines()]


target = sum(weights) // 4


def group_generator(num_group):
    # get all possible subsets of size num_group
    for group_1 in combinations(weights, num_group):
        # immediatly break if group_1 not the correct size
        if sum(group_1) != target:
            continue

        # remove group_1 from weights
        remaining_weights = [weight for weight in weights if weight not in group_1]

        # loop over all sizes for group_2
        for num_group_2 in range(len(remaining_weights)):
            # get this many values from remaining_weights
            for group_2 in combinations(remaining_weights, num_group_2):
                # only return if correct size
                if sum(group_2) != target:
                    continue

                remaining_weights_2 = [
                    weight for weight in remaining_weights if weight not in group_2
                ]

                for num_group_3 in range(len(remaining_weights_2)):
                    for group_3 in combinations(remaining_weights_2, num_group_3):
                        if sum(group_3) == target:
                            yield reduce(lambda x, y: x * y, group_1, 1)


num_group = 1
valid_qes = []
while True:
    for valid_qe in group_generator(num_group):
        valid_qes.append(valid_qe)

    if valid_qes:
        break
    num_group += 1
    if num_group > len(weights):
        print(":(")
        break

print(min(valid_qes))
