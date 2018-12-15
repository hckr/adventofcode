#!/usr/bin/env python3
import sys

tracks = {}
carts = []


def draw():
    for y in range(150):
        for x in range(150):
            for cart in carts:
                if cart['x'] == x and cart['y'] == y:
                    print(cart['dir'], end='')
                    break
            else:
                print(tracks.get((x, y), ' '), end='')
        print()
    print()


for y, line in enumerate(sys.stdin):
    for x, part in enumerate(line):
        if part in ('|', '-', '/', '\\', '+'):
            tracks[(x, y)] = part
        elif part in ('^', 'v', '<', '>'):
            carts.append({'x': x, 'y': y, 'dir': part, 'intersections': 0})
            if part in ('^', 'v'):
                tracks[(x, y)] = '|'
            elif part in ('<', '>'):
                tracks[(x, y)] = '-'

directions = ('^', '>', 'v', '<')
first_collision_printed = False

while True:
    carts.sort(key=lambda c: (c['y'], c['x']))
    to_be_removed = []

    for cart in carts:
        track = tracks[(cart['x'], cart['y'])]

        if track == '/':
            if cart['dir'] == '^':
                cart['dir'] = '>'
            elif cart['dir'] == '<':
                cart['dir'] = 'v'
            elif cart['dir'] == 'v':
                cart['dir'] = '<'
            elif cart['dir'] == '>':
                cart['dir'] = '^'
        elif track == '\\':
            if cart['dir'] == '^':
                cart['dir'] = '<'
            elif cart['dir'] == '<':
                cart['dir'] = '^'
            elif cart['dir'] == 'v':
                cart['dir'] = '>'
            elif cart['dir'] == '>':
                cart['dir'] = 'v'
        elif track == '+':
            intersections_modulo = cart['intersections'] % 3
            if intersections_modulo == 0:
                cart['dir'] = directions[(directions.index(cart['dir']) + 3) % 4]
            elif intersections_modulo == 2:
                cart['dir'] = directions[(directions.index(cart['dir']) + 1) % 4]
            cart['intersections'] += 1

        if cart['dir'] == '^':
            cart['y'] -= 1
        elif cart['dir'] == '>':
            cart['x'] += 1
        elif cart['dir'] == 'v':
            cart['y'] += 1
        elif cart['dir'] == '<':
            cart['x'] -= 1

        for other_cart in carts:
            if id(other_cart) == id(cart):
                continue
            if cart['x'] == other_cart['x'] and cart['y'] == other_cart['y']:
                if not first_collision_printed:
                    print(f"{cart['x']},{cart['y']}")
                    first_collision_printed = True
                to_be_removed.append(cart)
                to_be_removed.append(other_cart)
                removed = True

    for c in to_be_removed:
        carts.remove(c)

    if len(carts) == 1:
        print(f"{carts[0]['x']},{carts[0]['y']}")
        break
