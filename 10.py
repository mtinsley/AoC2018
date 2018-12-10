from collections import defaultdict
from lib import stdin_get_lines


def parse_line(line):
    x = line[10:16]
    y = line[17:24]
    vx = line[36:38]
    vy = line[39:42]

    return int(x), int(y), int(vx), int(vy)


def new_position(xy, vxy):
    return xy[0] + vxy[0], xy[1] + vxy[1]


def write_messages(lines):
    grid = defaultdict(set)
    for line in lines:
        x, y, vx, vy = parse_line(line)
        grid[(x, y)].add((vx, vy))

    in_threshold = False
    file_written = False
    iteration = 0
    threshold = 100
    while not (file_written and not in_threshold):
        iteration += 1
        new_grid = defaultdict(set)
        max_x = None
        min_x = None
        max_y = None
        min_y = None
        for xy, vs in grid.items():
            for vxy in vs:
                new_grid[new_position(xy, vxy)].add(vxy)
                max_x = max(max_x, xy[0]) if max_x is not None else xy[0]
                min_x = min(min_x, xy[0]) if min_x is not None else xy[0]
                max_y = max(max_y, xy[1]) if max_y is not None else xy[1]
                min_y = min(min_y, xy[1]) if min_y is not None else xy[1]
        grid = new_grid
        if (max_x - min_x) < threshold:
            in_threshold = True
            with open('out/' + str(iteration) + '.txt', 'w') as f:
                for y in range(min_y - 1, max_y + 1):
                    line = ''
                    for x in range(min_x - 1, max_x + 1):
                        line += '#' if (x, y) in grid and len(grid[(x, y)]) > 0 else ' '
                    f.write(line + "\n")
                file_written = True
        else:
            in_threshold = False


inp = stdin_get_lines()
write_messages(inp)
