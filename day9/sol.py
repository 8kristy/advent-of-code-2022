visited = []
head_pos = [0, 0]
tail_pos = [0, 0]

def move_head(dir):
    if dir == "R":
        head_pos[0] += 1
    elif dir == "U":
        head_pos[1] += 1
    elif dir == "L":
        head_pos[0] -= 1
    else:
        head_pos[1] -= 1

def move_tail(h_window):
    global tail_pos
    overlap = [value for value in get_window(tail_pos) if value in h_window]
    tail_pos = [x for x in overlap if x[0] == head_pos[0] or x[1] == head_pos[1]][0]
    visited.append(tail_pos)

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
            h_window = get_window(head_pos)
            if tail_pos not in h_window:
                move_tail(h_window)
            
visited = set([tuple(x) for x in visited])
print(len(visited))
