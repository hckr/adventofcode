#!/usr/bin/env python3
import sys
import re


def next_generation(state, notes, index_shift=0):
    dots_added_at_beginnig = (5 - len(re.search(r'^\.{0,5}', state).group(0)))
    index_shift -= dots_added_at_beginnig
    state = dots_added_at_beginnig * '.' + state + (5 - len(re.search(r'\.{0,5}$', state).group(0))) * '.'
    new_state = ['.' for _ in range(len(state))]
    for i in range(len(state) - 5 + 1):
        new_state[i+2] = notes.get(state[i:i+5], '.')
    return ''.join(new_state), index_shift


def count_value(state, index_shift=0):
    ans = 0
    for i, s in enumerate(state):
        if s == '#':
            ans += i + index_shift
    return ans


initial_state = input().split(' ')[-1]
input()  # skip empty line
notes = {}
for line in sys.stdin:
    template, result = re.findall(r'([#.]{5}) => ([#.])', line)[0]
    if result != '.':
        notes[template] = result

state = initial_state
index_shift = 0
for i in range(20):
    state, index_shift = next_generation(state, notes, index_shift)

print(count_value(state, index_shift))


target_generation = 50_000_000_000
state = initial_state
index_shift = 0
prev_value = -1
prev_diff = -1
how_many_same = 0
for i in range(target_generation):
    state, index_shift = next_generation(state, notes, index_shift)
    value = count_value(state, index_shift)
    diff = value - prev_value
    if diff == prev_diff:
        if how_many_same > 1000:
            print(prev_value + (target_generation - i) * diff)
            break
        else:
            how_many_same += 1
    prev_value = value
    prev_diff = diff
