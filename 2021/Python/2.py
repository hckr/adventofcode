import fileinput
from typing import Optional


def main(input_path: Optional[str] = None):
    """
    >>> main('../2.in')
    1989014
    2006917119
    """
    commands = [line.split() for line in fileinput.input(input_path)]

    # part 1
    horizontal = 0
    depth = 0
    for cmd, arg in commands:
        if cmd == "forward":
            horizontal += int(arg)
        elif cmd == "down":
            depth += int(arg)
        elif cmd == "up":
            depth -= int(arg)
        else:
            raise RuntimeError(f"unknown cmd {cmd}")
    print(horizontal * depth)

    # part 2
    horizontal = 0
    depth = 0
    aim = 0
    for cmd, arg in commands:
        if cmd == "down":
            aim += int(arg)
        elif cmd == "up":
            aim -= int(arg)
        elif cmd == "forward":
            horizontal += int(arg)
            depth += aim * int(arg)
        else:
            raise RuntimeError(f"unknown cmd {cmd}")
    print(horizontal * depth)


if __name__ == "__main__":
    main()
