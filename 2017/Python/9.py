#!/usr/bin/env python3

stream = input()

inside_garbage = False
ignore_next = False

score = 1
total_score = 0
non_cancelled_garbage = 0

for c in stream:
    if ignore_next == True:
        ignore_next = False
        continue
    if inside_garbage and c == '!':
        ignore_next = True
        continue
    if not inside_garbage and c == '<':
        inside_garbage = True
        continue
    if inside_garbage and c == '>':
        inside_garbage = False
        continue
    if inside_garbage:
        non_cancelled_garbage += 1
    if not inside_garbage:
        if c == '{':
            total_score += score
            score += 1
            continue
        if c == '}':
            score -= 1
            continue

print(total_score)
print(non_cancelled_garbage)
