import collections
import functools

from data.day7_data import data


def parse_rule(line: str):
    container, containee = line.split(" bags contain ")

    if containee == "no other bags.":
        return container, []

    bags = []
    for c in containee.split(", "):
        words = c.split(" ")
        quantity = int(words[0])
        bag = " ".join(words[1:3])
        bags.append((quantity, bag))

    return container, bags


def build_is_contained_by(rules):
    contained_by = collections.defaultdict(set)

    for container, content in rules:
        for _, bag in content:
            contained_by[bag].add(container)

    return contained_by


def build_contain(rules):
    return {container: set(content) for container, content in rules}


def all_valid_bags(target, contained_by):
    seen = set()
    to_visit: list = list(contained_by[target])
    valid_bags = set()

    while to_visit:
        candidate = to_visit.pop()
        if candidate in seen:
            continue

        valid_bags.add(candidate)
        seen.add(candidate)
        to_visit.extend({b for b in contained_by[candidate] if b not in seen})

    return valid_bags


def how_many_bags(target, contain):
    @functools.lru_cache()
    def how_many(target):
        to_visit = list(contain[target])
        count = 1

        while to_visit:
            number, bag = to_visit.pop()
            count += number * how_many(bag)

        return count

    # -1 because we don't want to count the first bag!
    return how_many(target) - 1


def solve_day7():
    print("Day 7", end=" ")

    rules = [parse_rule(x) for x in data]
    is_contained_by = build_is_contained_by(rules)
    can_contain_my_bag = all_valid_bags("shiny gold", is_contained_by)

    print(len(can_contain_my_bag), end=" ")

    contain = build_contain(rules)
    print(how_many_bags("shiny gold", contain))
