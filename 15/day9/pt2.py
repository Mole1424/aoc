from pathlib import Path
from collections import defaultdict

graph = defaultdict(list)
with Path("input.txt").open() as f:
    for line in f.read().splitlines():
        place1, _, place2, _, distance = line.split()
        graph[place1].append((place2, int(distance)))
        graph[place2].append((place1, int(distance)))


def dfs(current, visited, total_distance):
    if len(visited) == len(graph):
        return total_distance

    distances = []
    for neighbor, distance in graph[current]:
        if neighbor not in visited:
            visited.add(neighbor)
            distances.append(dfs(neighbor, visited, total_distance + distance))
            visited.remove(neighbor)

    return max(distances) if distances else float("-inf")


max_distance = float("-inf")
for start in graph:
    max_distance = max(max_distance, dfs(start, {start}, 0))
print(max_distance)
