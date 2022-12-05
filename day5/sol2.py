stacks = []

stacks_read = False

with open("input", 'r') as f:
    for line in f.readlines():
        line = line.strip()
        if (len(line) == 0):
            stacks_read = True
            continue
        
        if (not stacks_read):
            stacks.append([*line])
        else:
            move, number, from_x, x, to_y, y = line.split(" ")
            stacks[int(y) - 1] = stacks[int(y) - 1] + stacks[int(x) - 1][-int(number):]
            stacks[int(x) - 1] = stacks[int(x) - 1][:-int(number)]
                    
answer = ""
for stack in stacks:
    answer += stack.pop()       

print(answer) 