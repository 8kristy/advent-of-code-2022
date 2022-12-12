from dijkstar import Graph, find_path

def flatten_coords(x, y, lenghth):
    return x * lenghth + y


grid = []
graph = Graph()

with open("input", 'r') as f:
    for line in f.readlines():
        grid.append(list(line.strip()))

start_node = -1
end_node = -1

lowest_points = []

for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == "S":
            start_node = flatten_coords(i, j, len(grid[0]))
            grid[i][j] = "a"
        if grid[i][j] == "E":
            end_node = flatten_coords(i, j, len(grid[0]))
            grid[i][j] = "z"

for i in range(len(grid)):
    for j in range(len(grid[0])):

        if grid[i][j] == "a":
            lowest_points.append(flatten_coords(i, j, len(grid[0])))

        if i > 0 and ord(grid[i - 1][j]) - 1 <= ord(grid[i][j]):
            graph.add_edge(flatten_coords(i, j, len(grid[0])), flatten_coords(i - 1, j, len(grid[0])), 1)

        if i < len(grid) - 1 and ord(grid[i + 1][j]) - 1 <= ord(grid[i][j]):
            graph.add_edge(flatten_coords(i, j, len(grid[0])), flatten_coords(i + 1, j, len(grid[0])), 1)

        if j > 0 and ord(grid[i][j - 1]) - 1 <= ord(grid[i][j]):
            graph.add_edge(flatten_coords(i, j, len(grid[0])), flatten_coords(i, j - 1, len(grid[0])), 1)

        if j < len(grid[0]) - 1 and ord(grid[i][j + 1]) - 1 <= ord(grid[i][j]):
            graph.add_edge(flatten_coords(i, j, len(grid[0])), flatten_coords(i, j + 1, len(grid[0])), 1)

print(find_path(graph, start_node, end_node).total_cost)

min_path = 9999999999

for start in lowest_points:
    try:
        cost = find_path(graph, start, end_node).total_cost
        if cost < min_path:
            min_path = cost
    except:
        pass

print(min_path)