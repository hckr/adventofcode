import fileinput
from typing import Dict, List, Optional, Tuple

from sspipe import p, px  # type: ignore
from sspipe.pipe import Pipe  # type: ignore

Point = Tuple[int, int]
Line = Tuple[Point, Point]

# fmt: off

# my segments numbering
# clockwise from the top, middle is last
#  0000
# 5    1
# 5    1
#  6666
# 4    2
# 4    2
#  3333

digits_to_used_segments = {
    0: [0, 1, 2, 3, 4, 5   ],  # len 6
    1: [   1,    2         ],  # len 2; uniq len
    2: [0, 1,    3, 4,    6],  # len 5
    3: [0, 1, 2, 3,       6],  # len 5
    4: [   1,    2,    5, 6],  # uniq len
    5: [0,    2, 3,    5, 6],  # len 5
    6: [0,    2, 3, 4, 5, 6],  # len 6
    7: [0, 1, 2            ],  # len 3; uniq len
    8: [0, 1, 2, 3, 4, 5, 6],  # len 7; uniq len
    9: [0, 1, 2, 3,    5, 6],  # len 6
}

# len 6: 0, 6, 9
# [0, 1, 2, 3, 4, 5   ]  # 0 -> no 6
# [0,    2, 3, 4, 5, 6]  # 6 -> no 1
# [0, 1, 2, 3,    5, 6]  # 9 -> no 4

# len 5: 2, 3, 5
# [0, 1,    3, 4,    6]  # 2 -> no 2 and 5
# [0, 1, 2, 3,       6]  # 3 -> no 4 and 5
# [0,    2, 3,    5, 6]  # 5 -> no 1 and 4

# fmt: on


def main(input_path: Optional[str] = None):
    """
    >>> main('../8.in')
    367
    """
    signal_patterns, outputs = (
        fileinput.input(input_path) | p.map(px.strip().split(" | ")) | punzip
    )

    # part 1
    print(
        " ".join(outputs).split()
        | p.map(len)
        # fmt: off
        | p.where(lambda l: l in (2, # segments in digit 1
                                  4, #                   4
                                  3, #                   7
                                  7) #                   8
        )
        # fmt: on
        | p(list)
        | p(len)
    )

    # part 2
    for i, mapping in enumerate(map(decode_mapping, signal_patterns)):
        _digits = [
            decode_digit(letters, mapping)
            for letters in map(sort_letters, outputs[i].split())
        ]


def decode_mapping(_signal_patterns_row: List[str]) -> Dict[str, int]:
    # signal_patterns_row | p.map(px.split) | p.map(psort | pjoin) | plist
    return {}


def decode_digit(_letters: str, _mapping: Dict[str, int]) -> int:
    return 0


@Pipe
def punzip(iterable):
    return zip(*iterable)


@Pipe
def pjoin(substrings: List[str], separator: str = "") -> str:
    return separator.join(substrings)


@Pipe
def psort(iterable):
    return sorted(iterable)


@Pipe
def plist(iterable):
    return list(iterable)


def sort_letters(string: str) -> str:
    return string | psort | pjoin


if __name__ == "__main__":
    main()
