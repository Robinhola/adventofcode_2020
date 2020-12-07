def parse_rule(line: str):
    container, containee = line.split(' bags contain ')

    if containee == 'no other bags.':
        return container, []

    bags = []
    for c in containee.split(', '):
        words = c.split(' ')
        quantity = int(words[0])
        bag = ' '.join(words[1:3])
        bags.append((quantity, bag))

    return container, bags


def build_is_contained_by(rules):
    import collections
    contained_by = collections.defaultdict(set)

    for container, content in rules:
        for bag in content:
            contained_by[bag].add(container)

    return contained_by


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
        to_visit.append({b for b in contained_by[candidate] if b not in seen})

    return valid_bags
