from typing import List, Tuple

from data.day3_data import data


def how_many_trees_per_slope(forest: List[str], tree: str, slope: Tuple[int, int]) -> int:
    len_x,   len_y = len(forest[0]), len(forest)
    slope_x, slope_y = slope

    x = y = 0
    count = 0

    while y < len_y:
        if data[y][x] == tree:
            count += 1

        y += slope_y
        x = (x + slope_x) % len_x

    return count


def solve_day3():
    print('Day 3', end=' ')
    print(how_many_trees_per_slope(data, '#', (3, 1)), end=' ')

    numbers_of_trees = map(lambda slope: how_many_trees_per_slope(data, '#', slope), [
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2),
    ])

    product = 1
    for x in numbers_of_trees:
        product *= x
    print(product)


