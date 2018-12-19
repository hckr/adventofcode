__all__ = ['addr', 'addi', 'mulr', 'muli', 'banr', 'bani', 'borr', 'bori',
           'setr', 'seti', 'gtir', 'gtri', 'gtrr', 'eqir', 'eqri', 'eqrr']


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
