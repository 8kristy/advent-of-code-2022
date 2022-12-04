#
elves = []

with open("input", 'r') as f:
    temp_cals = 0
    for line in f.readlines():
        line = line.strip()
        if len(line) == 0:
            elves.append(temp_cals)
            temp_cals = 0
        else:
            temp_cals += int(line)
    elves.append(temp_cals)

print(max(elves))
elves.sort(reverse=True)
print(sum(elves[:3]))