from collections import defaultdict
from lib import stdin_get_lines


def parse_line(line):
    x = line[10:16]
    y = line[17:24]
    vx = line[36:38]
    vy = line[39:42]

    return int(x), int(y), int(vx), int(vy)


def new_position(xy, vxy):
    """
    Compute the new position for the given starting position (x, y) and velocity (vx, vy)
    """
    return xy[0] + vxy[0], xy[1] + vxy[1]


def write_messages(lines):
    grid = defaultdict(set)
    # Parse coordinates and velocities from lines
    for line in lines:
        x, y, vx, vy = parse_line(line)
        grid[(x, y)].add((vx, vy))

    in_threshold = False  # Indicates the point where files should start to be written (max_x - min_x)
    file_written = False
    iteration = 0
    threshold = 100
    while not file_written or in_threshold:
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
            # Start writing files when max_x - min_x is within the threshold
            # This reduces the number of files written to make it easier to locate the message
            in_threshold = True
            with open('out/' + str(iteration) + '.txt', 'w') as f:
                # Write characters between min/max y and min/max x
                # Write a '#' if x,y corresponds to a coordinate in the message, write a space ' ' otherwise
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
# The message (part 1) should be in one of the files written to the out directory
# The number of seconds required to reach that message (part 2) will be the name of the file
