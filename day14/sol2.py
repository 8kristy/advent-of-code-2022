rocks = []

with open("input", 'r') as f:
    for line in f.readlines():
        line = line.strip().split("->")
        line = [x.strip().split(",") for x in line]

        for i in range(len(line) - 1):
            x1, y1 = [int(x) for x in line[i]]
            x2, y2 = [int(x) for x in line[i + 1]]

            if x1 == x2:
                for y in range(min(y1, y2), max(y1, y2) + 1):
                    rocks.append((x1, y))

            elif y1 == y2:
                for x in range(min(x1, x2), max(x1, x2) + 1):
                    rocks.append((x, y1))

rocks = list(set(rocks))
max_depth = max([x[1] for x in rocks])

sand = []

while True:
    sand_x, sand_y = 500, 0
    while True:
        if sand_y == max_depth + 1:
            sand.append((sand_x, sand_y))
            break

        if (sand_x, sand_y + 1) not in rocks and (sand_x, sand_y + 1) not in sand:
            sand_y += 1
        elif (sand_x - 1, sand_y + 1) not in rocks and (sand_x - 1, sand_y + 1) not in sand:
            sand_x -= 1
            sand_y += 1
        elif (sand_x + 1, sand_y + 1) not in rocks and (sand_x + 1, sand_y + 1) not in sand:
            sand_x += 1
            sand_y += 1
        else:
            sand.append((sand_x, sand_y))
            break

    if sand_y == 0:
        break
    

print(len(sand))


          