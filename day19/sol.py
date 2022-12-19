from functools import cache

class Blueprint():

    def __init__(self, ore_ore_cost, clay_ore_cost, obsidian_ore_cost, obsidian_clay_cost, geode_ore_cost, geode_obsidian_cost):
        self.ore_ore_cost = ore_ore_cost
        self.clay_ore_cost = clay_ore_cost
        self.obsidian_ore_cost = obsidian_ore_cost
        self.obsidian_clay_cost = obsidian_clay_cost
        self.geode_ore_cost = geode_ore_cost
        self.geode_obsidian_cost = geode_obsidian_cost

blueprints = []

with open("input", 'r') as f:
    for line in f.readlines():
        b = [int(s) for s in line.split() if s.isdigit()]
        blueprints.append(Blueprint(b[0], b[1], b[2], b[3], b[4], b[5]))

@cache
def max_geodes(blueprint, ore_robots, clay_robots, obsidian_robots, geode_robots, ore, clay, obsidian, geodes, time):
    options = []

    if time == 0:
        return 0

    # buy geode robot
    if ore >= blueprint.geode_ore_cost and obsidian >= blueprint.geode_obsidian_cost:
        return geode_robots + max_geodes(blueprint, 
                              ore_robots, 
                              clay_robots, 
                              obsidian_robots, 
                              geode_robots + 1, 
                              ore + ore_robots - blueprint.geode_ore_cost, 
                              clay + clay_robots,
                              obsidian + obsidian_robots - blueprint.geode_obsidian_cost,
                              geodes + geode_robots,
                              time - 1)

    possible_obsidian = obsidian
    for i in range(0, time - 2):
        possible_obsidian += obsidian_robots + i
    if possible_obsidian < blueprint.geode_obsidian_cost:
        return geode_robots * time

    # buy nothing
    options.append(max_geodes(blueprint, 
                              ore_robots, 
                              clay_robots, 
                              obsidian_robots, 
                              geode_robots, 
                              ore + ore_robots, 
                              clay + clay_robots,
                              obsidian + obsidian_robots,
                              geodes + geode_robots,
                              time - 1))

    # buy ore robot
    if ore >= blueprint.ore_ore_cost:
        options.append(max_geodes(blueprint, 
                                ore_robots + 1, 
                                clay_robots, 
                                obsidian_robots, 
                                geode_robots, 
                                ore + ore_robots - blueprint.ore_ore_cost, 
                                clay + clay_robots,
                                obsidian + obsidian_robots,
                                geodes + geode_robots,
                                time - 1))

    # buy clay robot
    if ore >= blueprint.clay_ore_cost:
        options.append(max_geodes(blueprint, 
                                ore_robots, 
                                clay_robots + 1, 
                                obsidian_robots, 
                                geode_robots, 
                                ore + ore_robots - blueprint.clay_ore_cost, 
                                clay + clay_robots,
                                obsidian + obsidian_robots,
                                geodes + geode_robots,
                                time - 1))

    # buy obsidian robot
    if ore >= blueprint.obsidian_ore_cost and clay >= blueprint.obsidian_clay_cost:
        options.append(max_geodes(blueprint, 
                              ore_robots, 
                              clay_robots, 
                              obsidian_robots + 1, 
                              geode_robots, 
                              ore + ore_robots - blueprint.obsidian_ore_cost, 
                              clay + clay_robots - blueprint.obsidian_clay_cost,
                              obsidian + obsidian_robots,
                              geodes + geode_robots,
                              time - 1))

    return geode_robots + max(options)

total = 0

for i, blueprint in enumerate(blueprints):
    total += (i + 1) * max_geodes(blueprint, 1, 0, 0, 0, 0, 0, 0, 0, 24)

print(total)
