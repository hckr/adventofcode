#!/usr/bin/env python3
import sys
import re

part1_input, part2_input = sys.stdin.read().split('\n\n\n\n')

samples = []
for sample_lines in part1_input.split('\n\n'):
    before_line, instruction_line, after_line = sample_lines.split('\n')
    samples.append({
        'before': list(map(int, re.findall(r'(\d+), (\d+), (\d+), (\d+)', before_line)[0])),
        'instruction': list(map(int, instruction_line.split(' '))),
        'after': list(map(int, re.findall(r'(\d+), (\d+), (\d+), (\d+)', after_line)[0]))
    })


def addr(registers, instruction):
    opcode, a, b, c = instruction
    new_registers = registers[:]
    new_registers[c] = registers[a] + registers[b]
    return new_registers


def addi(registers, instruction):
    opcode, a, b, c = instruction
    new_registers = registers[:]
    new_registers[c] = registers[a] + b
    return new_registers


def mulr(registers, instruction):
    opcode, a, b, c = instruction
    new_registers = registers[:]
    new_registers[c] = registers[a] * registers[b]
    return new_registers


def muli(registers, instruction):
    opcode, a, b, c = instruction
    new_registers = registers[:]
    new_registers[c] = registers[a] * b
    return new_registers


def banr(registers, instruction):
    opcode, a, b, c = instruction
    new_registers = registers[:]
    new_registers[c] = registers[a] & registers[b]
    return new_registers


def bani(registers, instruction):
    opcode, a, b, c = instruction
    new_registers = registers[:]
    new_registers[c] = registers[a] & b
    return new_registers


def borr(registers, instruction):
    opcode, a, b, c = instruction
    new_registers = registers[:]
    new_registers[c] = registers[a] | registers[b]
    return new_registers


def bori(registers, instruction):
    opcode, a, b, c = instruction
    new_registers = registers[:]
    new_registers[c] = registers[a] | b
    return new_registers


def setr(registers, instruction):
    opcode, a, b, c = instruction
    new_registers = registers[:]
    new_registers[c] = registers[a]
    return new_registers


def seti(registers, instruction):
    opcode, a, b, c = instruction
    new_registers = registers[:]
    new_registers[c] = a
    return new_registers


def gtir(registers, instruction):
    opcode, a, b, c = instruction
    new_registers = registers[:]
    new_registers[c] = 1 if a > registers[b] else 0
    return new_registers


def gtri(registers, instruction):
    opcode, a, b, c = instruction
    new_registers = registers[:]
    new_registers[c] = 1 if registers[a] > b else 0
    return new_registers


def gtrr(registers, instruction):
    opcode, a, b, c = instruction
    new_registers = registers[:]
    new_registers[c] = 1 if registers[a] > registers[b] else 0
    return new_registers


def eqir(registers, instruction):
    opcode, a, b, c = instruction
    new_registers = registers[:]
    new_registers[c] = 1 if a == registers[b] else 0
    return new_registers


def eqri(registers, instruction):
    opcode, a, b, c = instruction
    new_registers = registers[:]
    new_registers[c] = 1 if registers[a] == b else 0
    return new_registers


def eqrr(registers, instruction):
    opcode, a, b, c = instruction
    new_registers = registers[:]
    new_registers[c] = 1 if registers[a] == registers[b] else 0
    return new_registers


opcodes = [addr, addi, mulr, muli, banr, bani, borr, bori, setr, seti, gtir, gtri, gtrr, eqir, eqri, eqrr]

behave_like_three_or_more = 0
for sample in samples:
    matching_opcodes = 0
    for opcode in opcodes:
        if sample['after'] == opcode(sample['before'], sample['instruction']):
            matching_opcodes += 1
        if matching_opcodes > 2:
            behave_like_three_or_more += 1
            break
print(behave_like_three_or_more)

possible_opcodes = []
for i in range(16):
    opcode_samples = list(filter(lambda s: s['instruction'][0] == i, samples))
    possible_opcodes.append(
        list(filter(lambda f: all(ops['after'] == f(ops['before'], ops['instruction'])
                    for ops in opcode_samples), opcodes)))

final_opcodes = possible_opcodes[:]
all_single = False
single = set()
while len(single) != 16:
    for i, opts in enumerate(final_opcodes):
        if isinstance(opts, list):
            if len(opts) == 1:
                single.add(opts[0])
                final_opcodes[i] = opts[0]
            else:
                final_opcodes[i] = list(filter(lambda x: x not in single, opts))

# print(final_opcodes)

registers = [0, 0, 0, 0]
for instruction_line in part2_input.strip().split('\n'):
    instruction = list(map(int, instruction_line.split(' ')))
    registers = final_opcodes[instruction[0]](registers, instruction)
print(registers[0])
