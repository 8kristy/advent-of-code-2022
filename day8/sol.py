trees = []

def is_visible(i, j):
    column = [x[j] for x in trees]

    left = trees[i][j] > max(trees[i][:j])
    right = trees[i][j] > max( trees[i][j + 1:])
    up = trees[i][j] > max(column[:i])
    down = trees[i][j] > max(column[i + 1:])
    
    return left or right or up or down

def can_see(i, j, start, end, dir, vertical):
    total = 0
    for x in range(start, end, dir):
        total += 1
        compare_to = trees[i][x]
        if vertical:
            compare_to = trees[x][j]
        if trees[i][j] <= compare_to:
            break
    return total

def get_scenic_score(i, j):
    left = can_see(i, j, j - 1, -1, -1, False)
    right = can_see(i, j, j + 1, len(trees[0]), 1, False)
    up = can_see(i, j, i - 1, -1, -1, True)
    down = can_see(i, j, i + 1, len(trees[0]), 1, True)
 
    return left * right * up * down

with open("input", 'r') as f:
    for line in f.readlines():
        trees.append(list(line.strip()))

visible = 2 * len(trees) + 2 * len(trees[0]) - 4
max_scenic_score = 0

for i in range(1, len(trees) - 1):
    for j in range(1, len(trees[0]) - 1):
        if is_visible(i, j):
            visible += 1
        scenic_score = get_scenic_score(i, j)
        if scenic_score > max_scenic_score:
            max_scenic_score = scenic_score

print(visible)
print(max_scenic_score)