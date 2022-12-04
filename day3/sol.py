priorities = 0

with open("input", 'r') as f:
    for line in f.readlines():
        l = int(len(line)/2)

        shared_char = list(set(line[:l]).intersection(set(line[l:])))[0]

        if shared_char.islower(): 
            priorities += ord(shared_char) - 96
        else:
            priorities += ord(shared_char) - 38

print(priorities)