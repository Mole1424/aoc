from pathlib import Path
from itertools import combinations

with Path("input.txt").open() as f:
    containers = list(map(int, f.read().splitlines()))

container_size = 150
ways = 0
for minimum_ways in range(1, len(containers) + 1):
    for combo in combinations(containers, minimum_ways):
        if sum(combo) == container_size:
            ways += 1
    if ways > 0:
        break
print(ways)
