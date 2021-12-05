import fileinput

import numpy as np


def main():
    input_iter = (line.strip() for line in fileinput.input())
    numbers = [int(x) for x in next(input_iter).split(",")]
    boards = []
    try:
        while True:
            assert next(input_iter) == ""
            boards.append(
                np.array([next(input_iter).split() for _ in range(5)], dtype=int)
            )
    except StopIteration:
        pass

    finished_boards = set()
    finished_board_scores = []  # just scores in order of winning (no mapping to boards)
    for number in numbers:
        for i, board in enumerate(boards):
            if i in finished_boards:
                continue
            board[board == number] = -1  # mutating board
            if (board == -1).all(axis=0).any() or (board == -1).all(axis=1).any():
                # found first winning board
                sum_of_unmarked = board[board != -1].sum()
                finished_boards.add(i)
                finished_board_scores.append(sum_of_unmarked * number)

    print(finished_board_scores[0])
    print(finished_board_scores[-1])


if __name__ == "__main__":
    main()
