from pathlib import Path
from itertools import combinations

with Path("input.txt").open() as f:
    boss_stats = tuple(  # (hp, damage, armour)
        int(stat) for line in f.read().splitlines() for _, stat in [line.split(": ")]
    )

weapons = [(8, 4), (10, 5), (25, 6), (40, 7), (74, 8)]
armours = [(0, 0), (13, 1), (31, 2), (53, 3), (75, 4), (102, 5)]
rings = [
    (0, 0, 0),
    (25, 1, 0),
    (50, 2, 0),
    (100, 3, 0),
    (20, 0, 1),
    (40, 0, 2),
    (80, 0, 3),
]

min_cost = float("inf")
for w_cost, w_dmg in weapons:
    for a_cost, a_arm in armours:
        for r1, r2 in combinations(rings, 2):
            cost = w_cost + a_cost + r1[0] + r2[0]
            dmg = w_dmg + r1[1] + r2[1]
            arm = a_arm + r1[2] + r2[2]

            player_stats = (100, dmg, arm)
            player_turns_to_win = -(
                -boss_stats[0] // max(1, player_stats[1] - boss_stats[2])
            )
            boss_turns_to_win = -(
                -player_stats[0] // max(1, boss_stats[1] - player_stats[2])
            )
            if player_turns_to_win <= boss_turns_to_win:
                min_cost = min(min_cost, cost)
print(min_cost)
