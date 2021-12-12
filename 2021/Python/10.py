import fileinput
from collections import deque
from typing import Deque, Optional, TypedDict

SYNTAX_ERROR_SCORES = {")": 3, "]": 57, "}": 1197, ">": 25137}
COMPLETION_SCORES = {")": 1, "]": 2, "}": 3, ">": 4}


def main(input_path: Optional[str] = None):
    r"""
    >>> from _pytest.monkeypatch import MonkeyPatch
    >>> with MonkeyPatch.context() as monkeypatch:
    ...     monkeypatch.setattr(fileinput, "input", lambda x: iter([
    ...         "[({(<(())[]>[[{[]{<()<>>\n",
    ...         "[(()[<>])]({[<{<<[]>>(\n",
    ...         "{([(<{}[<>[]}>{[]{[(<()>\n",
    ...         "(((({<>}<{<{<>}{[]{[]{}\n",
    ...         "[[<[([]))<([[{}[[()]]]\n",
    ...         "[{[{({}]{}}([{[{{{}}([]\n",
    ...         "{<[[]]>}<{[{[{[]{()[[[]\n",
    ...         "[<(<(<(<{}))><([]([]()\n",
    ...         "<{([([[(<>()){}]>(<<{{\n",
    ...         "<{([{{}}[<[[[<>{}]]]>[]]\n"]))
    ...     main()
    26397
    288957
    >>> main('../10.in')
    392139
    4001832844
    """
    lines = [line.strip() for line in fileinput.input(input_path)]

    # part 1
    syntax_error_score = 0
    for line in lines:
        error = get_first_error(line)
        if error:
            syntax_error_score += SYNTAX_ERROR_SCORES[error["found"]]
    print(syntax_error_score)

    # part2
    incomplete_lines = [line for line in lines if get_first_error(line) is None]
    completions = list(map(complete_line, incomplete_lines))
    completion_scores = list(map(completion_score, completions))
    middle_index = int((len(completion_scores) - 1) / 2)
    middle_score = sorted(completion_scores)[middle_index]
    print(middle_score)


class ValidationError(TypedDict):
    expected: str
    found: str
    position: int


OPEN_TO_CLOSE_CHARS = {"(": ")", "[": "]", "{": "}", "<": ">"}
OPEN_CHARS = set(OPEN_TO_CLOSE_CHARS.keys())
CLOSE_CHARS = set(OPEN_TO_CLOSE_CHARS.values())


def get_first_error(line: str) -> Optional[ValidationError]:
    currently_open: Deque[str] = deque()
    for pos, char in enumerate(line, start=1):
        if char in OPEN_CHARS:
            currently_open.append(char)
            continue
        if char in CLOSE_CHARS:
            last_opened = currently_open[-1]
            expected = OPEN_TO_CLOSE_CHARS[last_opened]
            if char == expected:
                currently_open.pop()
                continue
            return ValidationError(found=char, expected=expected, position=pos)
    return None


def complete_line(line: str) -> str:
    currently_open: Deque[str] = deque()
    for char in line:
        if char in OPEN_CHARS:
            currently_open.append(char)
            continue
        if char in CLOSE_CHARS:
            last_opened = currently_open[-1]
            expected = OPEN_TO_CLOSE_CHARS[last_opened]
            assert char == expected
            currently_open.pop()
    return "".join(OPEN_TO_CLOSE_CHARS[char] for char in reversed(currently_open))


def completion_score(completion: str):
    total = 0
    for char in completion:
        total = total * 5 + COMPLETION_SCORES[char]
    return total


if __name__ == "__main__":
    main()
