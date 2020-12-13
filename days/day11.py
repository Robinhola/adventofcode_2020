from typing import List
import itertools

import data.day11_data as d


def translate_grid(data: List[str]) -> List[List[int]]:
    output = [None] * len(data)
    for y, line in enumerate(data):
        output[y] = [None] * len(line)
        for x, c in enumerate(line):
            if c == "L":
                output[y][x] = 0
            if c == "#":
                output[y][x] = 1
            if c == ".":
                output[y][x] = 2
    return output


def create_neighbour_grid(grid: List[List[int]]) -> List[List[int]]:
    len_y = len(grid)
    len_x = len(grid[0])

    neighbours = [None] * len_y
    for y in range(len_y):
        neighbours[y] = [0] * len_x

    for y, x in itertools.product(range(len_y), range(len_x)):
        if grid[y][x] != 1:
            continue
        candidates = (
            (x - 1, y - 1), (x - 0, y - 1), (x + 1, y - 1),
            (x - 1, y - 0),                 (x + 1, y - 0),
            (x - 1, y + 1), (x - 0, y + 1), (x + 1, y + 1),
        )
        candidates = filter(lambda c: 0 <= c[0] < len_x, candidates)
        candidates = filter(lambda c: 0 <= c[1] < len_y, candidates)
        for i, j in candidates:
            neighbours[j][i] += 1

    return neighbours


def update_grid(grid: List[List[int]], numbers_of_neighbours, tolerance) -> bool:
    len_y = len(grid)
    len_x = len(grid[0])

    has_changed = False
    occupied_seats = 0

    for y, x in itertools.product(range(len_y), range(len_x)):
        v = grid[y][x]
        n = numbers_of_neighbours[y][x]
        new_value = v
        if v == 0 and n == 0:
            new_value = 1
        if v == 1 and n >= tolerance:
            new_value = 0

        has_changed |= new_value != v

        if new_value == 1:
            occupied_seats += 1

        grid[y][x] = new_value

    # from pprint import pprint
    # print("neigh then grid")
    # pprint(numbers_of_neighbours)
    # pprint(grid)

    return has_changed, occupied_seats

def count_occuped_seats_in_sight(grid: List[List[int]], x, y) -> int:
    count = 0

    def update_count(v) -> bool:
        nonlocal count
        count += 1 if v == 1 else 0
        return v != 2

    # Left and right
    for r in (range(x - 1, -1, -1), range(x + 1, len(grid[0]))):
        for ix in r:
            if update_count(grid[y][ix]): break

    # Up and Down
    for r in (range(y - 1, -1, -1), range(y + 1, len(grid))):
        for iy in r:
            if update_count(grid[iy][x]): break

    # Up Left
    i = 1
    while 0 <=  x - i and 0 <= y - i: 
        if update_count(grid[y - i][x - i]): break
        i += 1

    # Down Left
    i = 1
    while 0 <= x - i and y + i < len(grid): 
        if update_count(grid[y + i][x - i]): break
        i += 1

    # Up Right 
    i = 1
    while x + i < len(grid[0]) and 0 <= y - i: 
        if update_count(grid[y - i][x + i]): break
        i += 1

    # Down Right  
    i = 1
    while x + i < len(grid[0]) and y + i < len(grid): 
        if update_count(grid[y + i][x + i]): break
        i += 1

    return count


def create_in_sight_grid(grid) -> List[List[int]]:
    len_y = len(grid)
    len_x = len(grid[0])

    neighbours = [[0] * len_x for _ in range(len_y)]

    for y, x in itertools.product(range(len_y), range(len_x)):
        if grid[y][x] == 2: continue
        neighbours[y][x] = count_occuped_seats_in_sight(grid, x, y)

    return neighbours


def count_number_of_occupied_seats(data, neighbour_fn, tolerance) -> int:
    grid = translate_grid(data)
    has_changed = True
    occupied_seates = 0
    while has_changed:
        neighbours = neighbour_fn(grid)
        has_changed, occupied_seates = update_grid(grid, neighbours, tolerance)
    return occupied_seates 


def solve_day11():
    output = "Day 11 (unoptimized) "

    output += str(count_number_of_occupied_seats(d.sample_data, create_neighbour_grid, 4))
    # output += str(count_number_of_occupied_seats(d.data, create_neighbour_grid, 4))
    output += " "
    output += str(count_number_of_occupied_seats(d.sample_data, create_in_sight_grid, 5))
    # output += str(count_number_of_occupied_seats(d.data, create_in_sight_grid, 5))

    print(output, end=" ")
