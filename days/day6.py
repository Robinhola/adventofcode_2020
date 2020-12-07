from data.day6_data import data
from days.day4 import raw_lines_to_lines


def sum_cardinals(raw) -> int:
    characters = (set(x) for x in raw_lines_to_lines(raw))
    characters = map(lambda l: set(filter(lambda x: x != ' ', l)), characters)
    cardinals = map(lambda x: len(x), characters)
    return sum(cardinals)


def questions_everybody_answered_yes(raw: str) -> int:
    current_group = None
    groups = []
    for line in raw.split('\n'):
        if line:
            if current_group is None:
                current_group = set(line)
            else:
                current_group = current_group.intersection(set(line))
        else:
            groups.append(current_group)
            current_group = None

    cardinals = (len(x) for x in groups)
    return sum(cardinals)


def solve_day6():
    print("Day 6", end=' ')
    print(sum_cardinals(data), end=' ')
    print(questions_everybody_answered_yes(data))
