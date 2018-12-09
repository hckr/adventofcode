#!/usr/bin/env python3
import sys
import re
from collections import deque


def compute_scores(players, highest_marble):
    marbles = deque([0])

    scores = [0] * players
    current_player = 0

    for value in range(1, highest_marble + 1):
        if value % 23 != 0:
            marbles.rotate(2)
            marbles.append(value)
        else:
            scores[current_player] += value
            marbles.rotate(-7)
            scores[current_player] += marbles.pop()
        current_player = (current_player + 1) % players

    return scores


players, highest_marble = map(int, re.findall(r'\d+', sys.stdin.read()))
print(max(compute_scores(players, highest_marble)))
print(max(compute_scores(players, highest_marble * 100)))
