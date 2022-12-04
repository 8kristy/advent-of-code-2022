overlapping_pairs = 0
any_overlaps = 0

with open("input", 'r') as f:
    for line in f.readlines():
        pair1, pair2 = line.split(",")
        s1, e1 = [int(x) for x in pair1.split("-")]
        s2, e2 = [int(x) for x in pair2.split("-")]
        range1 = set(range(s1, e1 + 1))
        range2 = set(range(s2, e2 + 1))

        overlap = range1.intersection(range2)

        if overlap == range1 or overlap == range2:
            overlapping_pairs += 1

        if range1.intersection(range2):
            any_overlaps += 1

print(overlapping_pairs)
print(any_overlaps)