import sys
import math


def main():
    safe_reports = 0
    for line in sys.stdin:
        arr = list(map(int, line.split()))
        if is_report_valid(arr):
            safe_reports += 1
    print(safe_reports)
    # TODO: part 2
    # if one error can be tolerated, then the approach should be changed in full
    # two lists should be produced
    # one counting the sign and the other if the diff was in the range
    # as long as only one index (the same in both lists) is wrong, it's correct


def is_report_valid(arr: list[int]):
    pos_sign = True if arr[1] - arr[0] > 0 else False
    # print(list(zip(arr[:-1], arr[1:])))
    for a, b in zip(arr[:-1], arr[1:]):
        # print(a, b, pos_sign)
        diff = b - a
        cur_pos_sign = True if diff > 0 else False
        if abs(diff) < 1 or abs(diff) > 3:
            # print('beep')
            return False
        if cur_pos_sign is not pos_sign:
            # print('boop', cur_pos_sign, pos_sign)
            return False
    return True


if __name__ == "__main__":
    main()
