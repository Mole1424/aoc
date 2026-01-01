from pathlib import Path

with Path("input.txt").open() as f:
    strings = f.read().splitlines()

num_nice = 0

for string in strings:
    pairs = {}
    has_double_pair = False

    for i in range(len(string) - 1):
        pair = string[i : i + 2]
        if pair in pairs and i - pairs[pair] >= 2:
            has_double_pair = True
            break
        pairs.setdefault(pair, i)

    if (
        any(string[i] == string[i + 2] for i in range(len(string) - 2))
        and has_double_pair
    ):
        num_nice += 1

print(num_nice)
