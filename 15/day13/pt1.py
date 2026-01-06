from pathlib import Path
from collections import defaultdict
from itertools import permutations

happiness_graph = defaultdict(dict)
with Path("input.txt").open() as f:
    for line in f.read().splitlines():
        name1, _, gain_loose, units, _, _, _, _, _, _, name2 = line[:-1].split()
        happiness_graph[name1][name2] = int(units) * (1 if gain_loose == "gain" else -1)


max_happiness = float("-inf")
for seating_plan in permutations(happiness_graph.keys()):
    current_happiness = 0

    for i in range(len(seating_plan)):
        person = seating_plan[i]
        left_neighbor = seating_plan[(i - 1) % len(seating_plan)]
        right_neighbor = seating_plan[(i + 1) % len(seating_plan)]

        current_happiness += happiness_graph[person][left_neighbor]
        current_happiness += happiness_graph[person][right_neighbor]

    max_happiness = max(max_happiness, current_happiness)

print(max_happiness)
