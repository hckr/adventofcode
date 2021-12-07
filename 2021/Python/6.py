import fileinput
from typing import Optional


def main(input_path: Optional[str] = None):
    """
    >>> from _pytest.monkeypatch import MonkeyPatch
    >>> with MonkeyPatch.context() as monkeypatch:
    ...     monkeypatch.setattr(fileinput, "input", lambda x: iter(["3,4,3,1,2"]))
    ...     main()
    5934
    26984457539
    >>> main('../6.in')
    366057
    1653559299811
    """
    initial_timers = [
        int(x) for x in next(fileinput.input(input_path)).strip().split(",")
    ]

    # part 1
    timers = initial_timers
    for _day in range(80):
        new_timers = []
        for timer in timers:
            if timer == 0:
                new_timers.append(6)
                new_timers.append(8)
            else:
                new_timers.append(timer - 1)
        timers = new_timers
    print(len(timers))

    # part 2 - naive solution takes too much time
    timer_vals = {k: 0 for k in range(0, 9)}
    for t in initial_timers:
        timer_vals[t] += 1
    for _day in range(256):
        new_to_be_added = timer_vals[0]
        timer_vals[0] = 0
        for k in range(1, 9):
            timer_vals[k - 1] = timer_vals[k]
        timer_vals[6] += new_to_be_added
        timer_vals[8] = new_to_be_added
    print(sum(timer_vals.values()))


if __name__ == "__main__":
    main()
