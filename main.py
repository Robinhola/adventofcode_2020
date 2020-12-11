# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# Press the green button in the gutter to run the script.
from days.day1 import solve_day1
from days.day2 import solve_day2
from days.day3 import solve_day3
from days.day4 import solve_day4
from days.day5 import solve_day5
from days.day6 import solve_day6
from days.day7 import solve_day7
from days.day8 import solve_day8
from days.day9 import solve_day9
from days.day10 import solve_day10
from days.day11 import solve_day11

import time 

def solve(fn):
    start = time.time_ns()
    fn()
    end = time.time_ns()
    print(f"in {(end - start)/1_000_000}ms")

if __name__ == "__main__":
    solve(solve_day1)
    solve(solve_day2)
    solve(solve_day3)
    solve(solve_day4)
    solve(solve_day5)
    solve(solve_day6)
    solve(solve_day7)
    solve(solve_day8)
    solve(solve_day9)
    solve(solve_day10)
    solve(solve_day11)
