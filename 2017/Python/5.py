#!/usr/bin/env python3

orig_instructions = []

try:
    while True:
        orig_instructions.append(int(input()))
except EOFError:
    pass

## PART 1

instructions = list(orig_instructions)
pc = 0
s1 = 0

while pc < len(instructions):
    s1 += 1
    new_pc = pc + instructions[pc]
    instructions[pc] += 1
    pc = new_pc

print(s1)

## PART 2

instructions = list(orig_instructions)
pc = 0
s2 = 0

while pc < len(instructions):
    s2 += 1
    new_pc = pc + instructions[pc]
    if instructions[pc] >= 3:
        instructions[pc] -= 1
    else:
        instructions[pc] += 1
    pc = new_pc

print(s2)
