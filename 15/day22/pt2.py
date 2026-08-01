import sys
from pathlib import Path

# (mana, damage, health)
power_ups = [(53, 4, 0), (73, 2, 2)]
# (type, mana, magnitude, length)
effects = [("shield", 113, 7, 6), ("poison", 173, 3, 6), ("recharge", 229, 101, 5)]
abilities = power_ups + effects

# set up all initial stats
player_mana = 500
player_hp = 50
with Path("input.txt").open() as f:
    boss_hp, boss_damage = tuple(
        int(stat) for line in f.read().splitlines() for _, stat in [line.split(": ")]
    )


def apply_effects(current_effects, boss_hp, player_mana):
    new_effects = []
    player_armour = 0
    for type, magnitude, length in current_effects:
        if type == "shield":
            player_armour = magnitude
        elif type == "poison":
            boss_hp -= magnitude
        elif type == "recharge":
            player_mana += magnitude
        length -= 1
        if length != 0:
            new_effects.append((type, magnitude, length))
    return new_effects, boss_hp, player_mana, player_armour


# dijkstra? all possible outcomes (dumb (branching factor is <= 5) but should work?)
states = [(0, boss_hp, player_hp, player_mana, [])]
seen = set()

while len(states) != 0:
    # get state with lowest current_mana
    lowest_mana = float("inf")
    current_state = None
    for state in states:
        if state[0] < lowest_mana:
            lowest_mana = state[0]
            current_state = state
    mana_spent, boss_hp, player_hp, player_mana, current_effects = current_state  # type: ignore
    states.remove(current_state)  # type: ignore

    # check if weve been here before
    state_key = (boss_hp, player_hp, player_mana, tuple(current_effects))
    if state_key in seen:
        continue
    seen.add(state_key)

    # player's turn

    # hard difficulty
    player_hp -= 1
    if player_hp <= 0:
        continue

    # apply effects
    current_effects, boss_hp, player_mana, player_armour = apply_effects(
        current_effects, boss_hp, player_mana
    )

    if boss_hp <= 0:
        print(mana_spent)
        sys.exit()

    for ability in abilities:
        # copy states
        boss_hp_copy = boss_hp
        player_hp_copy = player_hp
        player_mana_copy = player_mana
        current_effects_copy = current_effects.copy()
        mana_spent_copy = mana_spent

        if isinstance(ability[0], str):
            # effect
            type, mana, magnitude, length = ability  # type: ignore
            # cannot use if effect already in current effect
            if player_mana_copy < mana or any(
                current_type == type for current_type, _, _ in current_effects_copy
            ):
                continue
            player_mana_copy -= mana
            mana_spent_copy += mana
            current_effects_copy.append((type, magnitude, length))
        else:
            # power_up
            mana, damage, health = ability  # type: ignore
            if player_mana_copy < mana:  # type: ignore
                continue
            boss_hp_copy -= damage
            player_hp_copy += health

            player_mana_copy -= mana  # type: ignore
            mana_spent_copy += mana  # type: ignore

        # boss' turn

        # apply effects
        current_effects_copy, boss_hp_copy, player_mana_copy, player_armour = (
            apply_effects(current_effects_copy, boss_hp_copy, player_mana_copy)
        )

        if boss_hp_copy <= 0:
            print(mana_spent_copy)
            sys.exit()

        player_hp_copy -= max(1, boss_damage - player_armour)

        # if can play on, add current state to the queue
        if player_hp_copy > 0 and player_mana_copy >= 53:
            states.append(
                (
                    mana_spent_copy,
                    boss_hp_copy,
                    player_hp_copy,
                    player_mana_copy,
                    current_effects_copy,
                )
            )
