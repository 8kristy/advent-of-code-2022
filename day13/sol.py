import json, itertools

def compare_lists(list1, list2):
    for left, right in itertools.zip_longest(list1, list2):
        if right == None:
            return False
        if left == None: 
            return True

        if type(left) is list and type(right) is not list:
            right = [right]

        if type(left) is not list and type(right) is list:
            left = [left]

        if type(left) is list and type(right) is list:
            recursed = compare_lists(left, right)
            if recursed != None:
                return recursed

        if left < right:
            return True

        if left > right:
            return False

with open("input", 'r') as f:
    lines = f.readlines()

right_order = 0

for i in range(0, len(lines), 3):
    list1 = json.loads(lines[i])
    list2 = json.loads(lines[i + 1])
    if compare_lists(list1, list2):
        right_order += int(i / 3 + 1)

print(right_order)

        
