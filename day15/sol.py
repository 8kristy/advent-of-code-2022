beacon_cant_be_at = set()
y = 2000000

with open("input", 'r') as f:
    for line in f.readlines():
        sensor, beacon = line.strip().split(":")
        sensor_x, sensor_y = [int(x.strip().split("=")[1]) for x in sensor.strip().split(",")]
        beacon_x, beacon_y = [int(x.strip().split("=")[1]) for x in beacon.strip().split(",")]

        manhattan_distance =  abs(sensor_x - beacon_x) + abs(sensor_y - beacon_y)
        start_x1 = sensor_x - manhattan_distance
        start_x2 = sensor_x + manhattan_distance

        for i in range(manhattan_distance):
            x1 = start_x1 + i
            x2 = start_x2 - i
            if sensor_y + i == y:
                cant_be_up = set([(x, sensor_y + i) for x in range(x1, x2)])
                beacon_cant_be_at = beacon_cant_be_at.union(cant_be_up)

            if sensor_y - i == y:
                cant_be_down = set([(x, sensor_y - i) for x in range(x1, x2)])
                beacon_cant_be_at = beacon_cant_be_at.union(cant_be_down)

print(len(beacon_cant_be_at))
