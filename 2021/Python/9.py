import fileinput
from typing import Optional

import numpy as np


def main(input_path: Optional[str] = None):
    r"""
    >>> from _pytest.monkeypatch import MonkeyPatch
    >>> with MonkeyPatch.context() as monkeypatch:
    ...     monkeypatch.setattr(fileinput, "input", lambda x: iter([
    ...         "2199943210\n",
    ...         "3987894921\n",
    ...         "9856789892\n",
    ...         "8767896789\n",
    ...         "9899965678\n"]))
    ...     main()
    15
    >>> main('../9.in')
    452
    """
    heightmap = np.array(
        [list(line.strip()) for line in fileinput.input(input_path)], dtype=int
    )
    diff_top = np.concatenate(
        [filler((1, heightmap.shape[1])), heightmap[1:] - heightmap[:-1]], axis=0
    )
    diff_right = np.concatenate(
        [heightmap[:, :-1] - heightmap[:, 1:], filler((heightmap.shape[0], 1))], axis=1
    )
    diff_bottom = np.concatenate(
        [heightmap[:-1] - heightmap[1:], filler((1, heightmap.shape[1]))], axis=0
    )
    diff_left = np.concatenate(
        [filler((heightmap.shape[0], 1)), heightmap[:, 1:] - heightmap[:, :-1]], axis=1
    )
    filter_low_points = (diff_top < 0) & (diff_right < 0) & (diff_bottom < 0) & (diff_left < 0)
    print(sum(heightmap[filter_low_points] + 1))


def filler(shape):
    return np.ones(shape) * -10

if __name__ == "__main__":
    main()
