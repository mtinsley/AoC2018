from string import ascii_lowercase
from sys import stdin


def day_five_part_one(data):
    """
    Remove repeated, alternating uppercase/lowercase characters until none remain in data.
    Return the length of the resulting data
    """
    last_len = len(data)
    while True:
        for lower in ascii_lowercase:
            upper = lower.upper()
            data = data.replace(lower + upper, '').replace(upper + lower, '')
        if last_len == len(data):
            break  # Break if the data wasn't changed in this pass

        last_len = len(data)

    return len(data)


def day_five_part_two(data):
    """
    For each letter, determine the length of the resulting data if that letter is removed from the string (upper and lowercase)
    """
    lengths = {}
    for lower in ascii_lowercase:
        upper = lower.upper()
        new_data = data.replace(lower, '').replace(upper, '')
        lengths[lower] = day_five_part_one(new_data)

    return min(lengths.values())


stdin = stdin.read().strip()

print('Part One: {0}'.format(day_five_part_one(stdin)))
print('Part Two: {0}'.format(day_five_part_two(stdin)))
