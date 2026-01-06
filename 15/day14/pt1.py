from pathlib import Path

with Path("input.txt").open() as f:
    stats = f.read().splitlines()

best_distance = 0
time = 2503
for stat in stats:
    _, _, _, speed, _, _, speed_time, _, _, _, _, _, _, rest_time, _ = stat.split()
    speed = int(speed)
    speed_time = int(speed_time)
    rest_time = int(rest_time)

    total_time = speed_time + rest_time
    num_times = time // total_time
    remaining_time = time % total_time
    distance = num_times * speed * speed_time + min(remaining_time, speed_time) * speed

    best_distance = max(best_distance, distance)

print(best_distance)
