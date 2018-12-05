from string import ascii_lowercase
from sys import stdin


def day_five_part_one(data):
    last_len = len(data)
    while True:
        for lower in ascii_lowercase:
            upper = lower.upper()
            data = data.replace(lower + upper, '').replace(upper + lower, '')
        if last_len == len(data):
            break

        last_len = len(data)

    return len(data)


def day_five_part_two(data):
    lengths = {}
    for lower in ascii_lowercase:
        upper = lower.upper()
        new_data = data.replace(lower, '').replace(upper, '')
        lengths[lower] = day_five_part_one(new_data)

    return min(lengths.values())


stdin = stdin.read().strip()

print('Part One: {0}'.format(day_five_part_one(stdin)))
print('Part Two: {0}'.format(day_five_part_two(stdin)))
