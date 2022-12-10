important_cycles = [20, 60, 100, 140, 180, 220]
cycle = 1
register = 1
signal_strength = 0

image = ""

def check_signal_strenth():
    global signal_strength, image
    if cycle in important_cycles:
        signal_strength += cycle * register

def draw_pixel():
    global image
    if cycle % 40 - 1 in [register - 1, register, register + 1]:
        image += "#"
    else:
        image += "."

with open("input", 'r') as f:
    for line in f.readlines():
        instruction = line.strip().split(" ")
        if len(instruction) == 1:
            draw_pixel()
            cycle += 1
        else:
            draw_pixel()
            cycle += 1
            check_signal_strenth()
            draw_pixel()
            cycle += 1
            register += int(instruction[1])

        check_signal_strenth()

print(signal_strength)
print('\n'.join(image[i:i+40] for i in range(0, len(image), 40)))