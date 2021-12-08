import fileinput
import math
from typing import Optional


def main(input_path: Optional[str] = None):
    """
    >>> from _pytest.monkeypatch import MonkeyPatch
    >>> with MonkeyPatch.context() as monkeypatch:
    ...     monkeypatch.setattr(fileinput, "input", lambda x: iter(["16,1,2,0,4,2,7,1,2,14"]))
    ...     main()
    37
    168
    >>> main('../7.in')
    336131
    92676646
    """
    crab_positions = [
        int(x) for x in next(fileinput.input(input_path)).strip().split(",")
    ]
    fileinput.close()

    # part 1
    middle_val = sorted(crab_positions)[(len(crab_positions) - 1) // 2]
    print(sum(abs(x - middle_val) for x in crab_positions))

    # part 2
    mean = sum(crab_positions) / len(crab_positions)
    print(
        min(
            sum(triangular_number(abs(x - mean_int)) for x in crab_positions)
            for mean_int in (math.floor(mean), math.ceil(mean))
        )
    )


def triangular_number(n: int):
    """
    >>> triangular_number(4)  # 4 + 3 + 2 + 1
    10
    """
    assert n >= 0
    return n * (n + 1) // 2


if __name__ == "__main__":
    main()
