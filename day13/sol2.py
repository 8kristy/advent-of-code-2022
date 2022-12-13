import json, itertools, functools

def compare_lists(list1, list2):
    for left, right in itertools.zip_longest(list1, list2):
        if right == None:
            return -1
        if left == None: 
            return 1

        if type(left) is list and type(right) is not list:
            right = [right]

        if type(left) is not list and type(right) is list:
            left = [left]

        if type(left) is list and type(right) is list:
            recursed = compare_lists(left, right)
            if recursed != None:
                return recursed
        try:
            if left < right:
                return 1

            if left > right:
                return -1
        except:
            pass

with open("input", 'r') as f:
    lines = f.readlines()

lists = []

for i in range(0, len(lines), 3):
    list1 = json.loads(lines[i])
    list2 = json.loads(lines[i + 1])
    lists.append(list1)
    lists.append(list2)

lists.append([[2]])
lists.append([[6]])

lists = sorted(lists, key=functools.cmp_to_key(compare_lists), reverse=True)

print((lists.index([[2]]) + 1) * (lists.index([[6]]) + 1))

        
