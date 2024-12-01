from collections import defaultdict
import fileinput
import itertools
from typing import Dict, Iterable, List, Optional, Tuple


def main(input_path: Optional[str] = None):
    r"""
    >>> from _pytest.monkeypatch import MonkeyPatch
    >>> with MonkeyPatch.context() as monkeypatch:
    ...     monkeypatch.setattr(fileinput, "input", lambda x: iter([
    ...         "NNCB\n",
    ...         "\n",
    ...         "CH -> B\n",
    ...         "HH -> N\n",
    ...         "CB -> H\n",
    ...         "NH -> C\n",
    ...         "HB -> C\n",
    ...         "HC -> B\n",
    ...         "HN -> C\n",
    ...         "NN -> C\n",
    ...         "BH -> H\n",
    ...         "NC -> B\n",
    ...         "NB -> B\n",
    ...         "BN -> B\n",
    ...         "BB -> N\n",
    ...         "BC -> B\n",
    ...         "CN -> C\n"]))
    ...     main()
    1588
    >>> main('../14.in')
    """
    input_iter = (line.strip() for line in fileinput.input(input_path))

    template = next(input_iter)
    assert next(input_iter) == ""
    insertion_rules = {}
    for line in input_iter:
        pair, insertion = line.split(" -> ")
        insertion_rules[tuple(pair)] = insertion

    # print(template, insertion_rules)

    # part 1
    result_1 = template
    for _ in range(40):
        print(_)
        result_1 = apply_rules(insertion_rules, 1, result_1)
    print("".join(result_1))
    # occurences = defaultdict(int)
    # for letter in result_1:
    #     occurences[letter] += 1
    # occ_sort = sorted(occurences.items(), key=lambda x: x[1])
    # print(occ_sort[-1][1] - occ_sort[0][1])


def apply_rules(
    insertion_rules: Dict[Tuple[str, str], str],
    template: str | List[str],
    steps: int,
    occurences: Optional[Dict[str, int]] = None
) -> List[str]:
    if occurences is None:
        occurences = defaultdict(int)
    result = [template[0]]
    for pair in itertools.pairwise(template):
        result.append(insertion_rules[pair])
        result.append(pair[1])
    return result


def sum_occurences(a: Dict[str, int], b: Dict[str, int]) -> Dict[str, int]:
    """
    >>> sum_occurences({'a': 3, 'b': 1}, {'a': 1, 'c': 2})
    {'a': 4, 'b': 1, 'c': 2}
    """
    result = dict(a)
    for key in b:
        if key in result:
            result[key] += b[key]
        else:
            result[key] = b[key]
    return result


if __name__ == "__main__":
    main()
