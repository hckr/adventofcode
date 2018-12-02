#!/usr/bin/env python3
import sys


def count_chars(line):
    counts = {}
    for letter in line:
        counts[letter] = counts.get(letter, 0) + 1
    return counts


twos = 0
threes = 0

for line in sys.stdin:
    line = line.strip()
    counts = count_chars(line)
    has_twos = False
    has_threes = False
    for k, v in counts.items():
        if v == 2:
            has_twos = True
        elif v == 3:
            has_threes = True
    if has_twos:
        twos += 1
    if has_threes:
        threes += 1

print(twos * threes)
