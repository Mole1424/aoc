from pathlib import Path

stats = []
with Path("input.txt").open() as f:
    for stat in f.read().splitlines():
        _, _, _, speed, _, _, speed_time, _, _, _, _, _, _, rest_time, _ = stat.split()
        stats.append((int(speed), int(speed_time), int(rest_time)))

scores = [0] * len(stats)
distances = [0] * len(stats)
for time in range(2503):
    for i, (speed, speed_time, rest_time) in enumerate(stats):
        if (time % (speed_time + rest_time)) < speed_time:
            distances[i] += speed

    scores[distances.index(max(distances))] += 1

print(max(scores))
