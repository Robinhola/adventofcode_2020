from typing import List

from data.day2_data import data, sample_data


class DataLine:
    def __init__(self, input_string: str):
        # 6-9 z: qzzzzxzzfzzzz
        left_side, right_side = input_string.split(': ')
        limits, target = left_side.split(' ')
        lower_limit, upper_limit = limits.split('-')

        self.password = right_side
        self.target = target
        self.lower_limit = int(lower_limit)
        self.upper_limit = int(upper_limit)

    def assert_correctness(self) -> bool:
        count = self.password.count(self.target)
        return self.lower_limit <= count <= self.upper_limit

    def assert_correctness_2(self) -> bool:
        def is_in_range(limit) -> bool:
            return 0 <= limit < len(self.password)

        def is_target_in(position):
            in_range = is_in_range(position)
            return not in_range or (
                in_range and
                self.password[position] == self.target
            )

        return is_target_in(self.lower_limit - 1) != is_target_in(self.upper_limit - 1)


def parse_data(data: List[str]) -> List[DataLine]:
    for line in data:
        yield DataLine(line)


def debug_sample_data():
    for d in parse_data(sample_data):
        print(d.lower_limit, d.upper_limit, d.target, ': ', d.password)
        print(d.assert_correctness_2())


def solve_day2():
    print('Day 2', end=' ')

    count = 0
    for d in parse_data(data):
        count += 1 if d.assert_correctness() else 0
    print(count, end=' ')

    count = 0
    for d in parse_data(data):
        count += 1 if d.assert_correctness_2() else 0
    print(count, end=' ')

