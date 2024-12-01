import sys
from collections import defaultdict


def main():
    first = []
    second = []
    for line in sys.stdin:
        a, b = line.split()
        first.append(int(a))
        second.append(int(b))
    # print(first)
    # print(second)
    first.sort()
    second.sort()
    sum_of_distances = sum(map(lambda a, b: abs(a - b), first, second))
    print(sum_of_distances)

    similarity_score = 0
    counts_in_second = defaultdict(int)
    for x in second:
        counts_in_second[x] += 1
    for x in first:
        similarity_score += x * counts_in_second[x]
    print(similarity_score)


if __name__ == "__main__":
    main()
