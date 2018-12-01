#!/usr/bin/env python3
import sys

frequency = 0
previous_frequencies = set([frequency])

changes = [int(line) for line in sys.stdin]

while True:
    for change in changes:
        frequency += change
        if frequency in previous_frequencies:
            print(frequency)
            exit()
        previous_frequencies.add(frequency)
