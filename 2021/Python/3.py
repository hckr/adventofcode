import fileinput
from collections import defaultdict
from functools import partial
from typing import Callable, List, TypeVar

import numpy as np
from sspipe import p, px

T = TypeVar("T")


def main():
    binary_numbers = [list(line.strip()) for line in fileinput.input()]

    # part 1
    num_length = len(binary_numbers[0])
    gamma_rate = (
        range(num_length)
        | p.map(p(select_nth_for_each_in, binary_numbers, px) | p(most_common))
        | p(join_str)
        | p(bin_to_int)
    )
    epsilon_rate = (
        range(num_length)
        | p.map(p(select_nth_for_each_in, binary_numbers, px) | p(least_common))
        | p(join_str)
        | p(bin_to_int)
    )
    print(gamma_rate * epsilon_rate)

    # part 2
    oxygen_generator_rating = filter_by_criteria(
        binary_numbers, lambda bits: bits == 1 if np.mean(bits) >= 0.5 else bits == 0
    )
    co2_scrubber_rating = filter_by_criteria(
        binary_numbers, lambda bits: bits == 0 if np.mean(bits) >= 0.5 else bits == 1
    )
    print(oxygen_generator_rating * co2_scrubber_rating)


def select_nth_for_each_in(list_of_lists: List[List[T]], n: int) -> List[T]:
    """Create a new list by selecting the n-th element (counting from zero) of each sublist.

    >>> select_nth_for_each_in([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 0)
    [1, 4, 7]

    >>> select_nth_for_each_in([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1)
    [2, 5, 8]

    >>> select_nth_for_each_in([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 2)
    [3, 6, 9]
    """
    return [sublist[n] for sublist in list_of_lists]


def most_common(values: List[T]) -> T:
    """Finds (first) most common element in list

    >>> most_common([1,1,2,3,4,4,4,5,1,1])
    1

    >>> most_common([1,1,2,3,4,4,4,5])
    4
    """
    (most_common, _count) = sorted(
        count_occurences(values).items(), key=lambda x: x[1], reverse=True
    )[0]
    return most_common


def least_common(values: List[T]) -> T:
    """Finds (first) least common element in list

    >>> least_common([1,1,2,3,4,4,4,5,1,1])
    2

    >>> least_common([1,1,3,4,4,4,5])
    3
    """
    (most_common, _count) = sorted(
        count_occurences(values).items(), key=lambda x: x[1]
    )[0]
    return most_common


def join_str(substrings: List[str], separator: str = "") -> str:
    return separator.join(substrings)


def count_occurences(values: List[T]) -> T:
    occurences = defaultdict(int)
    for v in values:
        occurences[v] += 1
    return occurences


def bin_to_int(binary: str) -> int:
    return int(binary, 2)


def filter_by_criteria(
    binary_numbers: List[List[str]],
    bits_to_bool_filter: Callable[[np.ndarray], np.ndarray],
) -> int:
    candidates = np.array(binary_numbers)
    num_length = len(binary_numbers[0])
    for pos in range(num_length):
        bits = np.array(select_nth_for_each_in(candidates, pos), dtype=int)
        candidates = candidates[bits_to_bool_filter(bits)]
        if len(candidates) == 1:
            return candidates[0] | p(join_str) | p(bin_to_int)
    raise AssertionError("should not happen")


if __name__ == "__main__":
    main()
