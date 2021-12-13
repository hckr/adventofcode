from collections import defaultdict
import fileinput
from typing import DefaultDict, Dict, List, Optional


def main(input_path: Optional[str] = None):
    r"""
    >>> from _pytest.monkeypatch import MonkeyPatch
    >>> with MonkeyPatch.context() as monkeypatch:
    ...     monkeypatch.setattr(fileinput, "input", lambda x: iter([
    ...         "start-A\n",
    ...         "start-b\n",
    ...         "A-c\n",
    ...         "A-b\n",
    ...         "b-d\n",
    ...         "A-end\n",
    ...         "b-end\n"]))
    ...     main()
    10
    36
    >>> main('../12.in')
    4549
    120535
    """
    adjacency: DefaultDict[str, List[str]] = defaultdict(list)
    for path in fileinput.input(input_path):
        begin, end = path.strip().split("-")
        adjacency[begin].append(end)
        adjacency[end].append(begin)
    print(len(paths_between_1(adjacency, "start", "end")))
    print(len(paths_between_2(adjacency, "start", "end")))
    # might be a _fun_ task to try refactoring this to only have one function


def paths_between_1(adjacency: Dict[str, List[str]], start: str, target: str):
    finished_paths: List[List[str]] = []

    def recur(current_path: List[str]):
        last_node = current_path[-1]
        if last_node == target:
            finished_paths.append(current_path)
            return
        for next_node in adjacency[last_node]:
            if next_node[0].islower() and next_node in current_path:
                continue  # small caves can't be visited twice
            recur(current_path + [next_node])

    recur([start])

    return finished_paths


def paths_between_2(adjacency: Dict[str, List[str]], start: str, target: str):
    finished_paths: List[List[str]] = []

    def recur(current_path: List[str], limit: bool = False):
        last_node = current_path[-1]
        if last_node == target:
            finished_paths.append(current_path)
            return
        for next_node in adjacency[last_node]:
            if next_node == start:
                continue  # can't go back to start
            limit_inner = limit
            if next_node[0].islower():
                if next_node in current_path:
                    if limit_inner:
                        continue  # only one small cave can be visited twice
                    limit_inner = True
            recur(current_path + [next_node], limit_inner)

    recur([start])

    return finished_paths


if __name__ == "__main__":
    main()
