from sympy.ntheory import factorint, divisors
import numpy

monkeys = []
common_mod = 0

class Monkey():

    def __init__(self, items, operation, test, throw_true, throw_false):
        self.items = items
        self.operation = operation
        self.test = test
        self.throw_true = throw_true
        self.throw_false = throw_false
        self.items_inspected = 0

    def throw_items(self):
        for item in self.items:
            self.items_inspected += 1
            num = 0
            if self.operation[1] == "":
                num = item
            else:
                num = int(self.operation[1])
            
            if self.operation[0] == "+":
                item = item + num
            else:
                item = item * num

            item = item % common_mod      

            if item % self.test == 0:
                monkeys[self.throw_true].items.append(item)
            else:
                monkeys[self.throw_false].items.append(item)

        self.items = []

with open("input", 'r') as f:
    for _ in range(8):
        f.readline()
        items = [int(x) for x in f.readline().strip().split(":")[1].split(",")]
        (operator, num) = f.readline().strip().split("old")[1].split(" ")[1:]
        test = int(f.readline().strip().split(" ")[-1])
        throw_true = int(f.readline().strip().split(" ")[-1])
        throw_false = int(f.readline().strip().split(" ")[-1])
        monkeys.append(Monkey(items, (operator, num), test, throw_true, throw_false))
        f.readline()

common_mod = int(numpy.prod([x.test for x in monkeys]))

for i in range(10000):
    for monkey in monkeys:
        monkey.throw_items()

inspected = [monkey.items_inspected for monkey in monkeys]
inspected.sort(reverse=True)
print(inspected[0] * inspected[1])
        