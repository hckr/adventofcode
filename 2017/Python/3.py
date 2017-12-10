#!/usr/bin/env python3
import math
from enum import Enum

###
class Direction(Enum):
    LEFT = 0
    UP = 1
    RIGHT = 2
    DOWN = 3
    LAST = 4


def get_cell_pos(cell):
    a = math.ceil(math.sqrt(cell))
    if a % 2 == 0:
        a += 1

    diff = a**2 - cell

    origin_x = origin_y = int((a - 1) / 2)
    x = a - 1
    y = a - 1

    d = Direction(Direction.LEFT)
    while diff > 0:
        if diff >= a:
            c = a - 1
        else:
            c = diff
        if d == Direction.LEFT:
            x -= c
        elif d == Direction.UP:
            y -= c
        elif d == Direction.RIGHT:
            x += c
        elif d == Direction.DOWN:
            y += c
        diff -= c
        d = Direction(d.value + 1)

    return x - origin_x, y - origin_y
###

cell = int(input())

### PART 1 # kind of 'optimized' way

x, y = get_cell_pos(cell)
print(abs(x) + abs(y))

### PART 2 # the hard way

mem = { '0,0': 1 }

x = 0
y = 0

should_increment = False
d = Direction(Direction.RIGHT)

a = 0
cur_max = 1

while True:
    if d == Direction.LEFT:
        x -= 1
    elif d == Direction.UP:
        y -= 1
    elif d == Direction.RIGHT:
        x += 1
    elif d == Direction.DOWN:
        y += 1

    cur_val = 0
    cur_val += mem.get('{},{}'.format(x-1, y-1), 0)
    cur_val += mem.get('{},{}'.format(x-1, y), 0)
    cur_val += mem.get('{},{}'.format(x-1, y+1), 0)
    cur_val += mem.get('{},{}'.format(x, y-1), 0)
    cur_val += mem.get('{},{}'.format(x, y+1), 0)
    cur_val += mem.get('{},{}'.format(x+1, y-1), 0)
    cur_val += mem.get('{},{}'.format(x+1, y), 0)
    cur_val += mem.get('{},{}'.format(x+1, y+1), 0)

    if cur_val > cell:
        print(cur_val)
        break

    mem['{},{}'.format(x, y)] = cur_val

    a += 1
    if a == cur_max:
        a = 0
        d = Direction((d.value - 1) % 4)
        if should_increment:
            cur_max += 1
        should_increment = not should_increment
