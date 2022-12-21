numbers = []

with open("input", 'r') as f:
    for i, line in enumerate(f.readlines()):
        numbers.append([int(line.strip()), i])

for pos, i in enumerate(range(len(numbers))):
    curr_num = [x for x in numbers if x[1] == i][0]
    curr_index = numbers.index(curr_num)
    new_index = curr_index + curr_num[0] 
    numbers.insert(new_index % (len(numbers) - 1), numbers.pop(curr_index))

zero = [x for x in numbers if x[0] == 0][0]
zero_index = numbers.index(zero)

num1000th = numbers[(zero_index + 1000) % len(numbers)]
num2000th = numbers[(zero_index + 2000) % len(numbers)]
num3000th = numbers[(zero_index + 3000) % len(numbers)]

print(num1000th[0] + num2000th[0] + num3000th[0])