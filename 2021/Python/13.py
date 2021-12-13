import fileinput
import functools
from typing import List, Optional, Tuple

import numpy as np


def main(input_path: Optional[str] = None):
    r"""
    >>> from _pytest.monkeypatch import MonkeyPatch
    >>> with MonkeyPatch.context() as monkeypatch:
    ...     monkeypatch.setattr(fileinput, "input", lambda x: iter([
    ...         "6,10\n",
    ...         "0,14\n",
    ...         "9,10\n",
    ...         "0,3\n",
    ...         "10,4\n",
    ...         "4,11\n",
    ...         "6,0\n",
    ...         "6,12\n",
    ...         "4,1\n",
    ...         "0,13\n",
    ...         "10,12\n",
    ...         "3,4\n",
    ...         "3,0\n",
    ...         "8,4\n",
    ...         "1,10\n",
    ...         "2,14\n",
    ...         "8,10\n",
    ...         "9,0\n",
    ...         "\n",
    ...         "fold along y=7\n",
    ...         "fold along x=5\n"]))
    ...     main()
    17
    #####
    #   #
    #   #
    #   #
    #####
    <BLANKLINE>
    <BLANKLINE>
    >>> main('../13.in')
    755
    ###  #    #  #   ## ###  ###   ##   ##
    #  # #    # #     # #  # #  # #  # #  #
    ###  #    ##      # #  # ###  #  # #
    #  # #    # #     # ###  #  # #### # ##
    #  # #    # #  #  # # #  #  # #  # #  #
    ###  #### #  #  ##  #  # ###  #  #  ###
    """
    input_iter = (line.strip() for line in fileinput.input(input_path))

    points: List[Tuple[int, int]] = []
    max_x = 0
    max_y = 0
    for line in input_iter:
        if len(line) == 0:
            break
        x, y = [int(x) for x in line.strip().split(",")]
        if x > max_x:
            max_x = x
        if y > max_y:
            max_y = y
        points.append((x, y))

    points_array = np.zeros((next_odd(max_y + 1), next_odd(max_x + 1)), dtype=int)
    for x, y in points:
        points_array[y, x] = 1

    folds: List[Tuple[str, int]] = []
    for line in input_iter:
        axis, center = line.replace("fold along ", "").split("=")
        folds.append((axis, int(center)))

    after_first_fold = do_the_fold(points_array, folds[0])
    print(np.sum(after_first_fold > 0))

    after_all_folds = functools.reduce(do_the_fold, folds, points_array)
    for row in after_all_folds:
        print("".join((" " if val == 0 else "#") for val in row).rstrip())


def next_odd(number: int):
    if number % 2 == 0:
        return number + 1
    return number


def do_the_fold(points_array: np.ndarray, fold: Tuple[str, int]):
    axis, center = fold
    # it looks like the fold is always in half
    if axis == "y":
        assert center == int(points_array.shape[0] / 2)
        return points_array[:center, :] + np.flip(
            points_array[(center + 1) :, :], axis=0
        )
    # axis == 'x'
    assert center == int(points_array.shape[1] / 2)
    return points_array[:, :center] + np.flip(points_array[:, (center + 1) :], axis=1)


if __name__ == "__main__":
    main()
