#!/usr/bin/env python3
import sys
import math
from collections import defaultdict

locations = list((tuple(map(int, line.split(','))) for line in sys.stdin))
# print(locations)

locations_xs = [loc[0] for loc in locations]
locations_ys = [loc[1] for loc in locations]

min_x = min(locations_xs)
max_x = max(locations_xs)
min_y = min(locations_ys)
max_y = max(locations_ys)

# print('xs in [', min_x, ',', max_x, ']')
# print('ys in [', min_y, ',', max_y, ']')

nearest_locations = {}

for x in range(min_x, max_x + 1):
    for y in range(min_y, max_y + 1):
        nearest = None
        nearest_distance = math.inf
        same = False
        for (lx, ly) in locations:
            distance = abs(lx - x) + abs(ly - y)
            if distance < nearest_distance:
                same = False
                nearest = (lx, ly)
                nearest_distance = distance
            elif distance == nearest_distance:
                same = True
        nearest_locations[(x, y)] = nearest if not same else None

infinite_locs = set(dict(filter(lambda x: x[0][0] in (min_x, max_x) or x[0][1] in (min_y, max_y),
                                nearest_locations.items())).values())

counts = defaultdict(int)
for loc in filter(lambda l: l not in infinite_locs, nearest_locations.values()):
    if loc is None:
        continue
    counts[loc] += 1

print(sorted(counts.items(), key=lambda x: x[1], reverse=True)[0][1])

region = 0
# full retard brute-force
for x in range(min_x - 500, max_x + 501):
    for y in range(min_y - 500, max_y + 501):
        summed_distance = 0
        for (lx, ly) in locations:
            summed_distance += abs(lx - x) + abs(ly - y)
        if summed_distance < 10000:
            region += 1

print(region)

# used for drawing the sample input:
# for y in range(min_y, max_y + 1):
#     for x in range(min_x, max_x + 1):
#         if (x, y) in locations:
#             print(string.ascii_uppercase[locations.index((x, y))], end='')
#         else:
#             nearest = nearest_locations[(x, y)]
#             if nearest is not None:
#                 print(string.ascii_lowercase[locations.index(nearest)], end='')
#             else:
#                 print('.', end='')
#     print()
