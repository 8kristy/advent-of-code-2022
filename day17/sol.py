rock0 = [[0, 0], [1, 0], [2, 0], [3, 0]]
rock1 = [[1, 0], [0, -1], [1, -1], [2, -1], [1, -2]]
rock2 = [[2, 0], [2, -1], [0, -2], [1, -2], [2, -2]]
rock3 = [[0, 0], [0, -1], [0, -2], [0, -3]]
rock4 = [[0, 0], [1, 0], [0, -1], [1, -1]]

rocks = [rock0, rock1, rock2, rock3, rock4]
jets = ""
curr_jet_index = 0
curr_rock_index = 0
cave = []

def move_rock_down(rock):
    next_fall = [[x, y - 1] for [x, y] in rock]
    for next in next_fall:
        if next in cave or next[1] == -1:
            return [[x, y] for [x, y] in rock]

    return [[x, y - 1] for [x, y] in rock]

def move_rock_sideways(rock, dir):
    rock_xs = [x[0] for x in rock]
    
    if dir == "<" and 0 not in rock_xs:
        next_move = [[x - 1, y] for [x, y] in rock]
        for next in next_move:
            if next in cave:
                return rock
        return [[x - 1, y] for [x, y] in rock]
    
    if dir == ">" and 6 not in rock_xs:
        next_move = [[x + 1, y] for [x, y] in rock]
        for next in next_move:
            if next in cave:
                return rock
        return [[x + 1, y] for [x, y] in rock]

    return rock

def position_rock(rock, x_mod, y_mod):
    return [[x + x_mod, y + y_mod] for [x, y] in rock]

start_x = 2
start_y = 3

with open("input", 'r') as f:
    for line in f.readlines():
        jets = line

for i in range(2022):
    if i % 20 == 0:
        cave = [coord for coord in cave if coord[1] > (start_y - 50)]

    if len(cave) > 0:
        start_y = max([y[1] for y in cave]) + 3 - min([y[1] for y in rocks[curr_rock_index]]) + 1

    rock = position_rock(rocks[curr_rock_index], start_x, start_y)
    prev_y = -1
    while rock[0][1] != prev_y:
        prev_y = rock[0][1]
        rock = move_rock_sideways(rock, jets[curr_jet_index])
        rock = move_rock_down(rock)
        curr_jet_index = (curr_jet_index + 1) % len(jets)

    for coords in rock:
        cave.append(coords)

    curr_rock_index = (curr_rock_index + 1) % 5

print(max([y[1] for y in cave]) + 1)