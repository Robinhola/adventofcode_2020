import collections
from typing import List, Tuple

from data.day1_data import data


def sum2(numbers: List[int], target: int, valid_numbers = None) -> Tuple[int, int]:
    """
    Find the two numbers inside the provided numbers for which their sum is
    equal to the provided target and return them.

    :param numbers:
    :param target:
    :return:
    """
    if valid_numbers is None:
        valid_numbers = collections.Counter(numbers)

    for n in numbers:
        need = target - n
        count = valid_numbers[need]
        if count > 0:
            if (n == need and count > 1) or n != need:
                return (n, need)

    return None, None


def sum3(numbers: List[int], target: int) -> Tuple[int, int, int]:
    valid_numbers = collections.Counter(numbers)

    for x in numbers:
        need = target - x
        a, b = sum2(numbers, need, valid_numbers)
        if None not in (a, b):
            return x, a, b


def solve_day1():
    print("Day 1", end=' ')

    a, b = sum2(data, 2020)
    print(a * b, end=' ')

    a, b, c = sum3(data, 2020)
    print(a * b * c)


