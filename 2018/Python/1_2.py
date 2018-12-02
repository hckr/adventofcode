#!/usr/bin/env python3
import sys
from itertools import cycle

frequency = 0
previous_frequencies = set([frequency])

changes = map(int, sys.stdin)

for change in cycle(changes):
    frequency += change
    if frequency in previous_frequencies:
        print(frequency)
        exit()
    previous_frequencies.add(frequency)
