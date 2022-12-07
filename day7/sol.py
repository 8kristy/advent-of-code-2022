from anytree import Node, RenderTree, search

filetree = Node("/")
curr_dir = filetree

with open("input", 'r') as f:
    for line in f.readlines():
        #print(line)
        terminal_text = line.strip().split()
        if terminal_text[0] == "$":
            if terminal_text[1] == "cd":
                if terminal_text[2] == "..":
                    curr_dir = curr_dir.parent
                else:
                    if terminal_text[2] == "/":
                        curr_dir = filetree
                    else:
                        curr_dir = search.find(curr_dir, lambda node: node.name == (terminal_text[2]) and node.parent == curr_dir)
        elif terminal_text[0] == "dir":
            dir = Node(terminal_text[1], parent=curr_dir)
        else:
            f = Node(terminal_text[0], parent=curr_dir)

dir_sizes = {}
total = 0


for pre, fill, node in RenderTree(filetree):
    print("%s%s" % (pre, node.name))

def get_total_size(node):
    total = 0
    for pre, fill, node in RenderTree(node):
        if node.name.isdigit():
            total += int(node.name)
    return total

for pre, fill, node in RenderTree(filetree):
        if not node.name.isdigit():
            dir_sizes[node] = get_total_size(node)

print(dir_sizes)
total = 0

for dir in dir_sizes:
    if dir_sizes[dir] < 100000:
        total += dir_sizes[dir]

print(total)