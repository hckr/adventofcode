#!/usr/bin/env python3
import sys

box_ids = [line.strip() for line in sys.stdin]


def are_matching_boxes(box_id1, box_id2):
    differences = 0
    last_difference_pos = -1
    for i, char in enumerate(box_id1):
        if char == box_id2[i]:
            continue
        differences += 1
        if differences > 1:
            return False, None
        last_difference_pos = i
    if differences == 1:
        return True, last_difference_pos
    return False, None


for i, box_id1 in enumerate(box_ids):
    for j, box_id2 in enumerate(box_ids[i:]):
        found, pos = are_matching_boxes(box_id1, box_id2)
        if found:
            print(box_id1[:pos] + box_id1[pos+1:])
            exit(0)

print('not found')
