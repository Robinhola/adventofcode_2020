from data.day4_data import sample_data, raw_data

from typing import List


class Passport:
    def __init__(self, byr=None, iyr=None, eyr=None, hgt=None, hcl=None, ecl=None, pid=None, cid=None, line=''):
        self.byr = byr
        self.iyr = iyr
        self.eyr = eyr
        self.hgt = hgt
        self.hcl = hcl
        self.ecl = ecl
        self.pid = pid
        self.cid = cid
        self.line = line

    @classmethod
    def from_line(cls, line: str) -> "Passport":
        words = line.split(' ')
        key_values = [w.split(':') for w in words]
        try:
            values = {
                k: v for (k, v) in key_values
            }
            values['line'] = line
            return cls(**values)
        except:
            print(key_values)

    def is_valid(self) -> bool:
        invalid = None in (
            self.byr,
            self.iyr,
            self.eyr,
            self.hgt,
            self.hcl,
            self.ecl,
            self.pid,
        )
        return not invalid

    def is_really_valid(self) -> bool:
        if not self.is_valid():
            return False

        import string

        def is_date(value, min, max) -> bool:
            return value.isdigit() and len(value) == 4 and min <= int(value) <= max

        def is_hair_colour():
            valid = (
                len(self.hcl) == 7 and
                str(self.hcl).startswith('#') and
                all(c in string.hexdigits for c in self.hcl[1:])
            )
            return valid

        invalid = False in (
            is_date(self.byr, 1920, 2002),
            is_date(self.iyr, 2010, 2020),
            is_date(self.eyr, 2020, 2030),
            str(self.hgt[:-2]).isdigit() and (
                self.hgt[-2:] == 'cm' and 149 < int(self.hgt[:-2]) < 194 or
                self.hgt[-2:] == 'in' and 58  < int(self.hgt[:-2]) < 77
            ),
            is_hair_colour(),
            self.ecl in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth') and self.line.count('ecl') == 1,
            len(self.pid) == 9 and str(self.pid).isdigit(),
        )
        return not invalid


def raw_lines_to_lines(raw: str) -> List[str]:
    lines = []
    current_line = ""
    for line in raw.split('\n'):
        if line:
            current_line += line + ' '
        else:
            lines.append(current_line[:-1])
            current_line = ""

    return lines


def solve_day4():
    lines = raw_lines_to_lines(raw_data)
    passports = (Passport.from_line(line) for line in lines)
    passports = [p for p in passports if p.is_valid()]
    print("Day 4", end=' ')
    print(len(passports), end=" ")
    passports = [p for p in passports if p.is_really_valid()]
    print(len(passports))


