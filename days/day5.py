from typing import Tuple


def seat_id(row, column) -> int:
    return row * 8 + column


Row = Column = int


def binary_search(start, end, instructions) -> int:
    lower_limit = start
    upper_limit = end

    for c in instructions:
        diff = (upper_limit - lower_limit) // 2
        # print(upper_limit, lower_limit, diff)
        if c == 'F' or c == 'L':  # Front/Left mean take the lower half therefore update upper limit
            upper_limit = lower_limit + diff
        elif c == 'B' or c == 'R':  # Back/Right mean take the upper half therefore update lower limit
            lower_limit = lower_limit + diff
        else:
            assert False, c

    assert upper_limit - lower_limit == 1, (lower_limit, upper_limit)

    return lower_limit


def find_seat(instructions: str) -> Tuple[Row, Column]:
    row = binary_search(0, 128, instructions[:7])
    col = binary_search(0, 8, instructions[7:])
    return row, col


def solve_day5():
    print("Day 5", end=' ')

    seats = {r: [0] * 8 for r in range(128)}

    from data.day5_data import data
    maximum = float('-inf')
    for i in data:
        r, c = find_seat(i)
        seats[r][c] = 1
        maximum = max(seat_id(r, c), maximum)

    print(maximum, end=' ')

    sums = {r: sum(seats[r]) for r in range(128)}

    for r in range(1, 126):
        if sums[r] == 7 and sums[r - 1] == sums[r + 1] == 8:
            c = seats[r].index(0)
            print(seat_id(r, c), end=' ')
            break

