import enum
from typing import Tuple, List

import data.day8_data as data


class Command(enum.Enum):
    NOP = 'nop'
    ACC = 'acc'
    JMP = 'jmp'


def parse_command(line) -> Tuple[Command, int]:
    command, value = line.split(' ')
    return Command(command), int(value)


def execute_commands(commands: List[Tuple[Command, int]], infinite_loop=True) -> int:
    seen = set()
    accumulator = 0
    i = 0
    while 0 <= i < len(commands):
        if i in seen:
            return accumulator if infinite_loop else None
        else:
            seen.add(i)

        c, value = commands[i]
        if c == Command.NOP:
            i += 1
        elif c == Command.ACC:
            accumulator += value
            i += 1
        elif c == Command.JMP:
            i += value

    return accumulator


def backtrack_find_corrupted_line(commands) -> int:
    for i, (c, value) in enumerate(commands):
        save = c
        if c == Command.NOP:
            commands[i] = Command.JMP, value
        elif c == Command.JMP:
            commands[i] = Command.NOP, value
        else:
            continue

        accumulator = execute_commands(commands, infinite_loop=False)
        commands[i] = save, value
        if accumulator is not None:
            return accumulator


def solve_day8():
    commands = [parse_command(x) for x in data.data]
    print("Day 8", end=" ")

    print(execute_commands(commands), end=" ")
    print(backtrack_find_corrupted_line(commands))
