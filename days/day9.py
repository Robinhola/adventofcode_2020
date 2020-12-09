from data.day9_data import data, sample_data


def two_sum(target, numbers):
    for x in numbers:
        candidate = target - x
        if candidate in numbers:
            return True

    return False


def find_two_sum_number(data, length_of_preambule):
    available_options = set(data[0:length_of_preambule])

    for x in range(length_of_preambule, len(data)):

        if not two_sum(data[x], available_options):
            return data[x]

        available_options.remove(data[x - length_of_preambule])
        available_options.add(data[x])


def find_continuous_sum(target, numbers) -> tuple:
    first = 0
    current_sum = numbers[0] + numbers[1]

    for i in range(2, len(numbers)):
        x = numbers[i]
        current_sum += x

        while current_sum > target:
            current_sum -= numbers[first]
            first += 1

        if current_sum == target:
            subset = numbers[first:i + 1]
            return min(subset) + max(subset)
            

def solve_day9():
    target = find_two_sum_number(data, 25)

    print("Day 9", end=' ')
    print(target, end=" ")
    print(find_continuous_sum(target, data), end=' ')
