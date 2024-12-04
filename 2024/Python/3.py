import re
import sys


def main():
    memory = sys.stdin.read()
    result = 0
    for a, b in re.findall(r'mul\((\d+),(\d+)\)', memory):
        # print(a, b)
        result += int(a) * int(b)
    print(result)

    # part 2

    result2 = 0
    enabled = True
    for mul, a, b, do, dont in re.findall(
            r"(?:(mul)\((\d+),(\d+)\))|(?:(do)\(\))|(?:(don't)\(\))", memory):
        if mul and enabled:
            result2 += int(a) * int(b)
        if do:
            enabled = True
            continue
        if dont:
            enabled = False
            continue
    print(result2)


if __name__ == "__main__":
    main()
