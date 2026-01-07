from pathlib import Path
from itertools import combinations

with Path("input.txt").open() as f:
    containers = list(map(int, f.read().splitlines()))

container_size = 150
ways = 0
for num_containers in range(1, len(containers) + 1):
    for combo in combinations(containers, num_containers):
        if sum(combo) == container_size:
            ways += 1
print(ways)
