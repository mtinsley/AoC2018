from itertools import product
from lib import stdin_get_lines
import re

# For parsing values in format: #123 @ 3,2: 5x4
CLAIM_REGEX = re.compile('#(?P<id>\d+) @ (?P<offset_x>\d+),(?P<offset_y>\d+): (?P<width>\d+)x(?P<length>\d+)')


def parse_claim(claim: str):
    """
    Parse the given claim into a tuple (id, offset_x, offset_y, width, length)
    """
    return [int(x) for x in CLAIM_REGEX.match(claim).groups()]


def day_three_part_one(sequences):
    """
    Determine the number of squares that are claimed twice
    """
    squares = {}
    claims = map(parse_claim, sequences)
    for _, offset_x, offset_y, width, length in claims:
        coordinates = product(range(offset_x, offset_x + width), range(offset_y, offset_y + length))
        for c in coordinates:
            squares[c] = squares.get(c, 0) + 1

    return sum([1 for count in squares.values() if count > 1])


def day_three_part_two(sequences):
    squares = {}
    claims = [parse_claim(s) for s in sequences]  # Not using map because we need to iterate twice
    # Populate squares with the number of claims on that square
    for _, offset_x, offset_y, width, length in claims:
        coordinates = product(range(offset_x, offset_x + width), range(offset_y, offset_y + length))
        for c in coordinates:
            squares[c] = squares.get(c, 0) + 1

    # Iterate a second time to find a claim that does not overlap (ie all squares are claimed exactly once)
    for id, offset_x, offset_y, width, length in claims:
        overlap = False
        coordinates = product(range(offset_x, offset_x + width), range(offset_y, offset_y + length))
        for c in coordinates:
            if squares[c] > 1:
                overlap = True

        if not overlap:
            return id


stdin = stdin_get_lines()

print('Day Three')
print('Part One: {0}'.format(day_three_part_one(stdin)))
print('Part Two: {0}'.format(day_three_part_two(stdin)))
