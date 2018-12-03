#!/usr/bin/env python3
import sys


def count_chars(line):
    counts = {}
    for letter in line:
        counts[letter] = counts.get(letter, 0) + 1
    return counts


doubles = 0
triples = 0

for line in sys.stdin:
    line = line.strip()
    counts = count_chars(line)
    has_doubles = False
    has_triples = False
    for k, v in counts.items():
        if v == 2:
            has_doubles = True
        elif v == 3:
            has_triples = True
    if has_doubles:
        doubles += 1
    if has_triples:
        triples += 1

print(doubles * triples)
