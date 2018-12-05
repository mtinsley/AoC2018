from lib import hamming_distance, stdin_get_lines


def day_two_part_one(sequences):
    """
    In the given list of strings, count the number of strings that contain 2 instances and 3 instances of any character
    Return the product of those totals.
    """
    contains_two = 0
    contains_three = 0
    for s in sequences:
        # Build a dictionary where the keys are characters in s and the values are the number of occurrences of those
        # characters in s
        counts = {char: s.count(char) for char in s}
        if 2 in counts.values():
            contains_two += 1
        if 3 in counts.values():
            contains_three += 1

    return contains_two * contains_three


def day_two_part_two(sequences):
    """
    Find two strings with a hamming distance of one and return the intersection of those strings.
    """
    for x in sequences:
        for y in sequences:
            if hamming_distance(x, y) == 1:
                # Build a string that excludes mismatched characters between x and y
                return ''.join([char for idx, char in enumerate(x) if x[idx] == y[idx]])


stdin = stdin_get_lines()

print('Day Two')
print('Part One: {0}'.format(day_two_part_one(stdin)))
print('Part Two: {0}'.format(day_two_part_two(stdin)))
