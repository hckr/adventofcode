#!/usr/bin/env python3

def cycle(start, length):
    index = start % length
    while True:
        yield index
        index = (index + 1) % length

def redistribute(memory_state):
    redist_index, redist_amount = max(enumerate(memory_state), key=lambda x: x[1])
    index_cycler = cycle(redist_index + 1, memory_state_len)

    memory_state[redist_index] = 0
    for i in index_cycler:
        if redist_amount == 0:
            break
        memory_state[i] += 1
        redist_amount -= 1

###

memory_state = [ int(x) for x in input().split() ]
memory_state_len = len(memory_state)

## PART 1

prev = set()
s1 = 0

while tuple(memory_state) not in prev:
    prev.add(tuple(memory_state))
    s1 += 1
    redistribute(memory_state)

print(s1)

## PART 2

wanted_state = list(memory_state)
s2 = 0

while True:
    s2 += 1
    redistribute(memory_state)
    if memory_state == wanted_state:
        break

print(s2)
