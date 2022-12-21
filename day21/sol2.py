from anytree import Node

monkeys = {}

with open("input", 'r') as f:
    for line in f.readlines():
        monkey_name, yells = line.strip().split(":")
        yells = yells.strip()

        if monkey_name == "root":
            num1, op, num2 = yells.split(" ")
            yells = num1 + " = " + num2

        if monkey_name == "humn":
            yells = "x"

        monkeys[monkey_name] = yells
        
def buildTree(node):
    if node.isdigit() or node == "x":
        return Node(node)
    else: 
        num1, op, num2 = node.split(" ")
        parent_node = Node(op)
        left_node = buildTree(monkeys[num1])
        left_node.parent = parent_node
        right_node = buildTree(monkeys[num2])
        right_node.parent = parent_node
        return parent_node

tree = buildTree(monkeys["root"])

def traverse(node):
    rep = ""
    if node.name.isdigit() or node.name == "x":
        return node.name
    
    rep += traverse(node.children[0])
    rep += node.name
    rep += traverse(node.children[1])
    return "(" + rep + ")"

print(traverse(tree))
print("^ Throw this into something like https://www.mathpapa.com/simplify-calculator/ to solve")