def find_start(line, chars):
    for i in range(len(line)):
        window = line[i:i+chars]
        if len(window) == len(set(window)):
            print(i+chars)
            break

with open("input", 'r') as f:
    line = f.readline().strip()
    find_start(line, 4)
    find_start(line, 14)