visited = []
knots = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]

def move_head(dir):
    if dir == "R":
        knots[0][0] += 1
    elif dir == "U":
        knots[0][1] += 1
    elif dir == "L":
        knots[0][0] -= 1
    else:
        knots[0][1] -= 1

def move_knot(i):
    if knots[i] not in get_window(knots[i - 1]):
        overlap = [value for value in get_window(knots[i]) if value in get_window(knots[i - 1])]
        knots[i] = [x for x in overlap if x[0] == knots[i - 1][0] or x[1] == knots[i - 1][1]][0]
        if i == 9:
            visited.append(knots[i])

def get_window(coords):
    cells = []
    for i in range(coords[0] - 1, coords[0] + 2):
        for j in range(coords[1] - 1, coords[1] + 2):
            cells.append([i, j])
    return cells

with open("input", 'r') as f:
    visited.append([0, 0])
    for line in f.readlines():
        move_dir, move_amount =  line.strip().split(" ")
        move_amount = int(move_amount)

        for i in range(move_amount):
            move_head(move_dir)
            for i in range(1, len(knots)):
                move_knot(i)
            
visited = set([tuple(x) for x in visited])
print(len(visited))
