#!/usr/bin/env python3
import sys
from functools import reduce


def required_fuel(mass):
    return max(0, mass // 3 - 2)


def real_required_fuel(mass):
    fuel = required_fuel(mass)
    additional_fuel = required_fuel(fuel)
    while additional_fuel > 0:
        fuel += additional_fuel
        additional_fuel = required_fuel(additional_fuel)
    return fuel


if __name__ == "__main__":
    masses = list(map(int, sys.stdin))

    # part one
    print(reduce(lambda fuel, mass: fuel + required_fuel(mass), masses, 0))

    # part two
    print(reduce(lambda fuel, mass: fuel + real_required_fuel(mass), masses, 0))
