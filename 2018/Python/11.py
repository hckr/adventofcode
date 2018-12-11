#!/usr/bin/env python3
import sys
import numpy as np  # numpy ftw, with plain lists it took forever

grid_serial_number = int(input())


def power_level(x, y):
    global grid_serial_number
    rack_id = x + 10
    return ((rack_id * y + grid_serial_number) * rack_id) // 10**2 % 10 - 5


power_levels = np.array([
    [power_level(x+1, y+1) for y in range(300)]
    for x in range(300)
])


# inefficient, yet working; btw same algo in C++ is over 5x faster
def best_square(size=3):
    global power_levels
    highest_power = 0
    coordinates = None
    for x in range(301-size):
        for y in range(301-size):
            square_power = np.sum(power_levels[x:x+size, y:y+size])
            # for i in range(size):
            #     for j in range(size):
            #         square_power += power_levels[x+i][y+j]
            if square_power > highest_power:
                highest_power = square_power
                coordinates = (x+1, y+1)
    return coordinates, highest_power


def best_square_any_size(min_size, max_size):
    highest_power = 0
    coordinates = None
    best_size = 0
    for size in range(min_size, max_size + 1):
        sys.stderr.write(f'\rTrying sqare size {size}...')
        coords, power = best_square(size)
        if power > highest_power:
            highest_power = power
            coordinates = coords
            best_size = size
    sys.stderr.write('\n')
    return (*coordinates, best_size)


print(','.join(map(str, best_square_any_size(1, 300))))
