number_monkeys = {}
operation_monkeys = {}

with open("input", 'r') as f:
    for line in f.readlines():
        monkey_name, yells = line.strip().split(":")
        yells = yells.strip()
        if yells.isdigit():
            number_monkeys[monkey_name] = int(yells)
        else:
            operation_monkeys[monkey_name] = yells

while operation_monkeys:
    keys_to_remove = []

    for monkey in operation_monkeys.keys():
        num1, op, num2 = operation_monkeys[monkey].split(" ")

        if num1 in number_monkeys and num2 in number_monkeys:
            val = str(number_monkeys[num1]) + op + str(number_monkeys[num2])
            number_monkeys[monkey] = int(eval(val))
            keys_to_remove.append(monkey)
        
    for key in keys_to_remove:
        operation_monkeys.pop(key, None)

print(number_monkeys["root"])