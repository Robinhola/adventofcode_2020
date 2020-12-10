import collections

import data.day10_data as d


def distribution_of_differences(data):
    sorted_data = [0] + sorted(data)
    differences = collections.defaultdict(int)

    for i in range(1, len(sorted_data)):
        y = sorted_data[i - 1]
        x = sorted_data[i]
        differences[x - y] += 1

    # For the built-in adapter
    differences[3] += 1

    return differences


def count_number_of_distinct_arrangements(data):
    # n of arrangements at i
    # 0 1 4 5 6 7 10 11 12 15 16 19 22
    # 1 1 1 1 2 4  4  4  8  8  8  8  8
    sorted_data = [0] + sorted(data)
    sorted_data = sorted_data + [sorted_data[-1] + 3]
    arrangements = [None] * len(sorted_data)
    arrangements[0] = 1
    for i in range(1, len(sorted_data)):
        count = 0
        v = sorted_data[i]
        for j in range(1, 4):
            index = i - j
            if 0 <= index and v - sorted_data[index] < 4:
                count += arrangements[index]

        arrangements[i] = count

    # print(arrangements)
    return arrangements[-1]

def solve_day10():
    output = "Day 10 "

    differences = distribution_of_differences(d.data)
    output += str(differences[1] * differences[3]) + " "
    # output += str(count_number_of_distinct_arrangements(d.sample_data))
    # output += str(count_number_of_distinct_arrangements(d.sample_data2))
    output += str(count_number_of_distinct_arrangements(d.data))
    print(output, end=" ")
