from itertools import cycle
from lib import stdin_get_lines


def day_two_part_one(lines):
    """
    Iterate over lines and keep a running total of the frequency
    """
    res = 0
    for item in lines:
        sign = item[0]
        value = item[1:]
        if sign == '+':
            res += int(value)
        else:
            res -= int(value)

    return res


def day_two_part_two(lines):
    """
    Iterate over lines until a frequency is reached twice. Cycle over lines as many times as needed.
    """
    res = 0
    frequencies = set()
    frequencies.add(res)
    for item in cycle(lines):
        sign = item[0]
        value = item[1:]
        if sign == '+':
            res += int(value)
        else:
            res -= int(value)

        if res in frequencies:
            return res

        frequencies.add(res)


stdin = stdin_get_lines()

print('Day One')
print('Part One: {0}'.format(day_two_part_one(stdin)))
print('Part Two: {0}'.format(day_two_part_two(stdin)))
