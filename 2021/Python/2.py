import fileinput

commands = [line.split() for line in fileinput.input()]

# part 1
horizontal = 0
depth = 0
for cmd, arg in commands:
    if cmd == 'forward':
        horizontal += int(arg)
    elif cmd == 'down':
        depth += int(arg)
    elif cmd == 'up':
        depth -= int(arg)
    else:
        raise RuntimeError(f'unknown cmd {cmd}')
print(horizontal * depth)

# part 2
horizontal = 0
depth = 0
aim = 0
for cmd, arg in commands:
    if cmd == 'down':
        aim += int(arg)
    elif cmd == 'up':
        aim -= int(arg)
    elif cmd == 'forward':
        horizontal += int(arg)
        depth += aim * int(arg)
    else:
        raise RuntimeError(f'unknown cmd {cmd}')
print(horizontal * depth)
