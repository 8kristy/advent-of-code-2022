symbols = dict(
    A = 1,
    B = 2,
    C = 3,
    X = 0,
    Y = 3,
    Z = 6
)

to_win = dict([(1, 2), (2, 3), (3, 1)])
to_lose = dict([(1, 3), (2, 1), (3, 2)])

total_score = 0

with open("input", 'r') as f:
    for line in f.readlines():
        scores = [symbols[x] for x in line.strip().split(" ")]
        if scores[1] == 3:
            total_score += scores[0]
        elif scores[1] == 6:
            total_score += to_win[scores[0]]
        else:
            total_score += to_lose[scores[0]]
        total_score += scores[1]

print(total_score)
