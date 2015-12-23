# Not my solution, but  at least I fully understand this one now I've seen it :-)
# Messed about a bit with some of the loops to make things more readable/understandable

import itertools

# Weapons:    Cost  Damage  Armor
# Dagger        8     4       0
# Shortsword   10     5       0
# Warhammer    25     6       0
# Longsword    40     7       0
# Greataxe     74     8       0
weapons = (
    (8, 4, 0),
    (10, 5, 0),
    (25, 6, 0),
    (40, 7, 0),
    (74, 8, 0)
)


# Armor:      Cost  Damage  Armor
# Leather      13     0       1
# Chainmail    31     0       2
# Splintmail   53     0       3
# Bandedmail   75     0       4
# Platemail   102     0       5
armor = (
    (0, 0, 0),
    (13, 0, 1),
    (31, 0, 2),
    (53, 0, 3),
    (75, 0, 4),
    (102, 0, 5),
)


# Rings:      Cost  Damage  Armor
# Damage +1    25     1       0
# Damage +2    50     2       0
# Damage +3   100     3       0
# Defense +1   20     0       1
# Defense +2   40     0       2
# Defense +3   80     0       3
rings = (
    (0, 0, 0),
    (0, 0, 0),
    (25, 1, 0),
    (50, 2, 0),
    (100, 3, 0),
    (20, 0, 1),
    (40, 0, 2),
    (80, 0, 3),
)


def do_fight(player):
    # Hit Points: 103, Damage: 9, Armor: 2
    boss = [103, 9, 2]
    while True:
        boss[0] -= max(player[1] - boss[2], 1)
        if boss[0] <= 0:
            return True
        player[0] -= max(boss[1] - player[2], 1)
        if player[0] <= 0:
            return False

wins = []
# for weapon_cost, weapon_damage, _ in weapons:
for w in weapons:
    # for armor_cost, _, armor_armor in armor:
    for a in armor:
        for ring1, ring2 in itertools.combinations(rings, 2):
            damageVal = w[1] + ring1[1] + ring2[1]
            armorVal = a[2] + ring1[2] + ring2[2]
            if do_fight([100, damageVal, armorVal]):
                wins.append(w[0] + a[0] + ring1[0] + ring2[0])
print min(wins)

loses = []
for weapon_cost, weapon_damage, _ in weapons:
    for armor_cost, _, armor_armor in armor:
        for ring1, ring2 in itertools.combinations(rings, 2):
            if not do_fight([100, weapon_damage + ring1[1] + ring2[1], armor_armor + ring1[2] + ring2[2]]):
                loses.append(weapon_cost + armor_cost + ring1[0] + ring2[0])
print max(loses)
