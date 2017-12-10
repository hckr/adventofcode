#!/usr/bin/env python3

instructions = []
registers = {}

try:
    while True:
        ins = {}
        ins['reg'], ins['op'], ins['op_arg'], _, ins['cond'] = input().split(maxsplit=4)
        # adding 'x' before register name because some sames might be Python keywords, like 'is'
        ins['reg'] = 'x' + ins['reg']
        ins['op_arg'] = int(ins['op_arg'])
        ins['cond'] = 'x' + ins['cond']
        if ins['reg'] not in registers:
            registers[ins['reg']] = 0
        instructions.append(ins)
except EOFError:
    pass

s2 = 0

for ins in instructions:
    if eval(ins['cond'], globals(), registers):
        if ins['op'] == 'inc':
            registers[ins['reg']] += ins['op_arg']
        elif ins['op'] == 'dec':
            registers[ins['reg']] -= ins['op_arg']
        s2 = max(s2, registers[ins['reg']])

print(max(registers.values()))
print(s2)
