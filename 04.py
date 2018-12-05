from lib import stdin_get_lines
from collections import Counter


def day_four_part_one(sequences):
    entries = sorted(sequences)
    sleep_log = {}
    current_guard = None
    sleep_start = None
    for entry in entries:
        parts = entry.split(' ')
        minute = int(parts[1][3:5])
        if 'Guard' in entry:
            current_guard = int(entry.split(' ')[3][1:])
            if current_guard not in sleep_log:
                sleep_log[current_guard] = []
        if 'asleep' in entry:
            sleep_start = minute
        if 'wakes' in entry:
            for asleep in range(sleep_start, minute):
                sleep_log[current_guard].append(asleep)

    max_guard = max(sleep_log, key=lambda x: len(sleep_log[x]))
    c = Counter(sleep_log[max_guard])
    return max_guard * c.most_common(1)[0][0]


def day_four_part_two(sequences):
    entries = sorted(sequences)
    sleep_log = {}
    current_guard = None
    sleep_start = None
    for entry in entries:
        parts = entry.split(' ')
        minute = int(parts[1][3:5])
        if 'Guard' in entry:
            current_guard = int(entry.split(' ')[3][1:])
            if current_guard not in sleep_log:
                sleep_log[current_guard] = []
        if 'asleep' in entry:
            sleep_start = minute
        if 'wakes' in entry:
            for asleep in range(sleep_start, minute):
                sleep_log[current_guard].append(asleep)

    max_total = 0
    max_gaurd = None
    max_minute = None
    for guard, minutes in sleep_log.items():
        if len(minutes) == 0:
            continue
        c = Counter(sleep_log[guard])
        (minute, total) = c.most_common(1)[0]
        if total > max_total:
            max_gaurd = guard
            max_total = total
            max_minute = minute

    return max_gaurd * max_minute


stdin = stdin_get_lines()

print('Part One: {0}'.format(day_four_part_one(stdin)))
print('Part Two: {0}'.format(day_four_part_two(stdin)))
