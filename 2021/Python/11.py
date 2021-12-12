import fileinput
from typing import List, Optional, Set, Tuple

import numpy as np

ROWS = 10
COLS = 10


def main(input_path: Optional[str] = None):
    r"""
    >>> from _pytest.monkeypatch import MonkeyPatch
    >>> with MonkeyPatch.context() as monkeypatch:
    ...     monkeypatch.setattr(fileinput, "input", lambda x: iter([
    ...         "5483143223\n",
    ...         "2745854711\n",
    ...         "5264556173\n",
    ...         "6141336146\n",
    ...         "6357385478\n",
    ...         "4167524645\n",
    ...         "2176841721\n",
    ...         "6882881134\n",
    ...         "4846848554\n",
    ...         "5283751526\n"]))
    ...     main()
    1656
    195
    >>> main('../11.in')
    1632
    303
    """
    energies = np.array(
        [list(line.strip()) for line in fileinput.input(input_path)], dtype=int
    )

    flash_count = 0

    step = 0
    while True:
        step += 1
        new_energies = energies + 1

        already_flashed: Set[Tuple[int, int]] = set()
        while True:
            flashing = find_flashing(new_energies)
            not_yet_flashed = flashing - already_flashed
            if len(not_yet_flashed) == 0:
                break
            for i, j in not_yet_flashed:
                already_flashed.add((i, j))
                new_energies[adjacent_indices(i, j)] += 1

        if len(already_flashed) > 0:
            new_energies[tuple(zip(*already_flashed))] = 0
            flash_count += len(already_flashed)

        if step == 100:
            print(flash_count)

        if np.all(new_energies == 0):
            print(step)
            break  # assuming it'll always be after 100th step

        energies = new_energies


def find_flashing(energies: np.ndarray) -> Set[Tuple[int, int]]:
    return set(zip(*np.where(energies > 9)))


def adjacent_indices(i: int, j: int) -> Tuple[List[int], List[int]]:
    """
    >>> adjacent_indices(1, 1)
    ([0, 0, 0, 1, 1, 2, 2, 2], [0, 1, 2, 0, 2, 0, 1, 2])
    >>> adjacent_indices(0, 0)
    ([0, 1, 1], [1, 0, 1])
    >>> adjacent_indices(9, 9)
    ([8, 8, 9], [8, 9, 8])
    >>> adjacent_indices(8, 9)
    ([7, 7, 8, 9, 9], [8, 9, 8, 8, 9])
    """
    rows = []
    cols = []
    for a in range(max(0, i - 1), min(ROWS, i + 2)):
        for b in range(max(0, j - 1), min(COLS, j + 2)):
            if not (a == i and b == j):
                rows.append(a)
                cols.append(b)
    return rows, cols


if __name__ == "__main__":
    main()
