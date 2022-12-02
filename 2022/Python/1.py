import fileinput
from typing import Optional


def main(input_path: Optional[str] = None):
    calories_per_elf = [
        sum(int(x) for x in group.split('\n') if x != '')
        for group in ''.join(fileinput.input(input_path)).split('\n\n')
    ]

    # part 1
    print(max(calories_per_elf))

    # part 2
    print(sum(sorted(calories_per_elf, reverse=True)[:3]))


if __name__ == "__main__":
    main()
