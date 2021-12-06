import fileinput
from collections import defaultdict
from functools import partial
from itertools import chain, filterfalse
from typing import Dict, List, Optional, Tuple

from sspipe import p  # type: ignore

Point = Tuple[int, int]
Line = Tuple[Point, Point]


def main(input_path: Optional[str] = None):
    """
    >>> main('../5.in')
    7468
    22364
    """
    vent_lines = fileinput.input(input_path) | p.map(parse_line) | p(list)

    # part 1
    point_counts: Dict[Point, int] = defaultdict(int)
    for point in (
        vent_lines
        | p(partial(filterfalse, is_diagonal))
        | p.map(points_on_line)
        | p(partial(chain.from_iterable))
    ):
        point_counts[point] += 1
    print(point_counts.values() | p.where(lambda x: x >= 2) | p(list) | p(len))

    # part 2
    point_counts = defaultdict(int)
    for points in vent_lines | p.map(points_on_line):
        for point in points:
            point_counts[point] += 1
    print(point_counts.values() | p.where(lambda x: x >= 2) | p(list) | p(len))


def parse_line(line: str) -> Line:
    """
    >>> parse_line("1,2 -> 3,4")
    ((1, 2), (3, 4))
    """
    begin, end = line.strip().split(" -> ")
    return parse_point(begin), parse_point(end)


def parse_point(coords: str) -> Point:
    """
    >>> parse_point("1,2")
    (1, 2)
    """
    x, y = tuple(int(x) for x in coords.split(","))
    return x, y


def is_diagonal(line: Line) -> bool:
    (x1, y1), (x2, y2) = line
    return x1 != x2 and y1 != y2


def points_on_line(line: Line) -> List[Point]:
    (x1, y1), (x2, y2) = line
    if x1 == x2:
        return [(x1, y) for y in ic_range(y1, y2)]
    if y1 == y2:
        return [(x, y1) for x in ic_range(x1, x2)]
    if abs(x2 - x1) == abs(y2 - y1):
        return list(zip(ic_range(x1, x2), ic_range(y1, y2)))
    raise RuntimeError(
        "diagonal lines which are not exactly at 45 deg are not supported"
    )


def ic_range(start, end):
    """Inclusive consecutive range

    >>> list(ic_range(1, 3))
    [1, 2, 3]

    >>> list(ic_range(-3, 1))
    [-3, -2, -1, 0, 1]
    """
    step = 1
    if start > end:
        step = -1
    for x in range(start, end + step, step):
        yield x


if __name__ == "__main__":
    main()
