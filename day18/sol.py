cubes = []

with open("input", 'r') as f:
    for line in f.readlines():
        cubes.append([int(x) for x in line.strip().split(",")])

total_sides = len(cubes) * 6

for cube in cubes:
    if [cube[0] + 1, cube[1], cube[2]] in cubes:
        total_sides -= 1
    if [cube[0] - 1, cube[1], cube[2]] in cubes:
        total_sides -= 1
    if [cube[0], cube[1] + 1, cube[2]] in cubes:
        total_sides -= 1
    if [cube[0], cube[1] - 1, cube[2]] in cubes:
        total_sides -= 1
    if [cube[0], cube[1], cube[2] + 1] in cubes:
        total_sides -= 1
    if [cube[0], cube[1], cube[2] - 1] in cubes:
        total_sides -= 1

print(total_sides)

max_x = max(x[0] for x in cubes)
max_y = max(x[1] for x in cubes)
max_z = max(x[2] for x in cubes)

for i in range(max_x):
    for j in range(max_y):
        for k in range(max_z):
            if [i, j, k] not in cubes:
                midair = False
                if ([i + 1, j, k] not in cubes and 
                    [i - 1, j, k] not in cubes and 
                    [i, j + 1, k] not in cubes and 
                    [i, j - 1, k] not in cubes and 
                    [i, j, k + 1] not in cubes and 
                    [i, j, k - 1] not in cubes):
                    midair = True

                if not midair:
                    left = len([[x, y, z] for [x, y, z] in cubes if y == j and z == k and x < i]) > 0
                    right = len([[x, y, z] for [x, y, z] in cubes if y == j and z == k and x > i]) > 0
                    up = len([[x, y, z] for [x, y, z] in cubes if x == i and z == k and y < j]) > 0
                    down = len([[x, y, z] for [x, y, z] in cubes if x == i and z == k and y > j]) > 0
                    near = len([[x, y, z] for [x, y, z] in cubes if y == j and x == i and z < k]) > 0
                    far = len([[x, y, z] for [x, y, z] in cubes if y == j and x == i and z > k]) > 0

                    if left and right and up and down and near and far:
                        total_sides -= 6

print(total_sides)

