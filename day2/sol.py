symbols = dict(
    A = 1,
    B = 2,
    C = 3,
    X = 1,
    Y = 2,
    Z = 3
)

total_score = 0

with open("input", 'r') as f:
    for line in f.readlines():
        scores = [symbols[x] for x in line.strip().split(" ")]
        if scores[0] == scores[1]:
            total_score += 3
        elif (scores[0] == 3 and scores[1] == 1) or (scores[0] == 1 and scores[1] == 2) or (scores[0] == 2 and scores[1] == 3):
            total_score += 6
        
        total_score += scores[1]

print(total_score)
