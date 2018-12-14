#!/usr/bin/env python3

input = int(input())


def scores_after_n_receipes(n):
    scores = [3, 7]
    elfs_positions = [0, 1]
    target_scores = n + 10
    while len(scores) < target_scores:
        new_receipe_score = 0
        for i, pos in enumerate(elfs_positions):
            new_receipe_score += scores[pos]
        scores.extend(map(int, str(new_receipe_score)))
        for i, pos in enumerate(elfs_positions):
            elfs_positions[i] = (elfs_positions[i] + scores[pos] + 1) % len(scores)
        # debug_scores = scores[:]
        # for i, s in enumerate(debug_scores):
        #     if i not in elfs_positions:
        #         debug_scores[i] = f' {s} '
        # debug_scores[elfs_positions[0]] = f'({debug_scores[elfs_positions[0]]})'
        # debug_scores[elfs_positions[1]] = f'[{debug_scores[elfs_positions[1]]}]'
        # print(' '.join(map(str, debug_scores)))
    return scores[n:n+10]


def after_how_many(next_scores):
    scores = [3, 7]
    elfs_positions = [0, 1]
    target_len = len(next_scores)
    while True:
        new_receipe_score = 0
        for i, pos in enumerate(elfs_positions):
            new_receipe_score += scores[pos]
        for score in map(int, str(new_receipe_score)):
            scores.append(score)
            if ''.join(map(str, scores[-target_len:])) == next_scores:
                return len(scores) - target_len
        for i, pos in enumerate(elfs_positions):
            elfs_positions[i] = (elfs_positions[i] + scores[pos] + 1) % len(scores)


print(''.join(map(str, scores_after_n_receipes(input))))
print(after_how_many(str(input)))
