import fileinput
from typing import Optional


def main(input_path: Optional[str] = None):
    """
    >>> main('../1.in')
    1266
    1217
    """
    measurements = [int(line) for line in fileinput.input(input_path)]

    # part 1
    print(
        sum(
            1 if measurements[i] > measurements[i - 1] else 0
            for i in range(1, len(measurements))
        )
    )

    # part 2
    window_size = 3
    window_sums = [
        sum(measurements[i : i + window_size])
        for i in range(len(measurements) - window_size + 1)
    ]
    print(
        sum(
            1 if window_sums[i] > window_sums[i - 1] else 0
            for i in range(1, len(window_sums))
        )
    )


if __name__ == "__main__":
    main()
