priorities = 0

with open("input", 'r') as f:
    lines = [x.strip() for x in f.readlines()]
    for i in range(0, len(lines), 3):

        if (len(lines[i]) == 0):
            break

        shared_char = list(set(lines[i]).intersection(set(lines[i+1])).intersection(set(lines[i+2])))[0]
        if shared_char.islower(): 
            priorities += ord(shared_char) - 96
        else:
            priorities += ord(shared_char) - 38

print(priorities)