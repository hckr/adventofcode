import fileinput
import math
from collections import defaultdict
from queue import PriorityQueue
from typing import Dict, List, Optional, Tuple

import numpy as np

Coords = Tuple[int, int]


def main(input_path: Optional[str] = None):  # pylint: disable=too-many-locals
    r"""
    >>> from _pytest.monkeypatch import MonkeyPatch
    >>> with MonkeyPatch.context() as monkeypatch:
    ...     monkeypatch.setattr(fileinput, "input", lambda x: iter([
    ...         "1163751742\n",
    ...         "1381373672\n",
    ...         "2136511328\n",
    ...         "3694931569\n",
    ...         "7463417111\n",
    ...         "1319128137\n",
    ...         "1359912421\n",
    ...         "3125421639\n",
    ...         "1293138521\n",
    ...         "2311944581\n"]))
    ...     main()
    40
    315
    >>> main('../15.in')
    393
    2823
    """
    risk_map = np.array(
        [list(line.strip()) for line in fileinput.input(input_path)], dtype=int
    )
    rows, cols = risk_map.shape
    _path, total_risk = a_star(risk_map, (0, 0), (rows - 1, cols - 1))
    # print(path)
    print(total_risk)

    real_times_larger = 5
    real_rows = rows * real_times_larger
    real_cols = cols * real_times_larger
    real_risk_map = np.zeros((real_rows, real_cols), dtype=int)
    for row_offset in range(real_times_larger):
        for col_offset in range(real_times_larger):
            row_ind_start = row_offset * rows
            col_ind_start = col_offset * cols
            real_risk_map[
                row_ind_start : row_ind_start + rows,
                col_ind_start : col_ind_start + cols,
            ] = (
                risk_map + row_offset + col_offset
            )
    real_risk_map[real_risk_map > 9] -= 9
    _real_path, real_total_risk = a_star(
        real_risk_map, (0, 0), (real_rows - 1, real_cols - 1)
    )
    # print(real_path)
    print(real_total_risk)


# https://en.wikipedia.org/wiki/A*_search_algorithm
def a_star(
    risk_map: np.ndarray, start: Coords, goal: Coords
) -> Tuple[List[Coords], int]:
    assert len(risk_map.shape) == 2
    rows, cols = risk_map.shape

    open_set: "PriorityQueue[Tuple[int | float, Coords]]" = PriorityQueue()
    open_set.put((0, start))
    came_from: Dict[Coords, Coords] = {}

    # for node n, g_score[n] is the cost of the cheapest path from start to n currently known
    g_score: Dict[Coords, int | float] = defaultdict(lambda: math.inf)
    g_score[start] = 0

    # for node n, f_score[n] := gScore[n] + h(n). f_score[n] represents our current best guess as to
    # how short a path from start to finish can be if it goes through n.
    f_score: Dict[Coords, int | float] = defaultdict(lambda: math.inf)
    f_score[start] = distance(start, goal)

    while len(open_set.queue) > 0:
        # the node in open_set having the lowest f_score value
        current = open_set.get()[1]
        if current == goal:
            node = current
            total_path = []
            total_risk = 0
            while node != start:
                total_risk += risk_map[node]
                total_path.append(node)
                node = came_from[node]
            return list(reversed(total_path)), total_risk

        for neighbor in adjacent_nodes(current, rows, cols):
            # d(current, neighbor) is the weight of the edge from current to neighbor
            # tentative_g_score is the distance from start to the neighbor through current
            tentative_g_score = g_score[current] + risk_map[neighbor]
            if tentative_g_score < g_score[neighbor]:
                # this path to neighbor is better than any previous one. Record it!
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + distance(neighbor, goal)
                if not any(x[1] == neighbor for x in open_set.queue):
                    open_set.put((f_score[neighbor], neighbor))

    raise RuntimeError("Path not found. Shouldn't happen.")


def adjacent_nodes(coords: Coords, rows: int, cols: int) -> List[Coords]:
    """
    >>> adjacent_nodes((1, 1), 10, 10)
    [(0, 1), (1, 0), (1, 2), (2, 1)]
    >>> adjacent_nodes((0, 0), 10, 10)
    [(0, 1), (1, 0)]
    >>> adjacent_nodes((9, 9), 10, 10)
    [(8, 9), (9, 8)]
    >>> adjacent_nodes((8, 9), 10, 10)
    [(7, 9), (8, 8), (9, 9)]
    """
    adjacent = []
    i, j = coords
    for a in range(max(0, i - 1), min(rows, i + 2)):
        for b in range(max(0, j - 1), min(cols, j + 2)):
            if not (a == i and b == j) and (a == i or b == j):
                adjacent.append((a, b))
    return adjacent


def distance(coords1: Coords, coords2: Coords) -> int:
    return abs(coords1[0] - coords2[0]) + abs(coords1[1] - coords2[1])


def print_risk_map(risk_map: str):
    for row in risk_map:
        print("".join(str(x) for x in row))


if __name__ == "__main__":
    main()
