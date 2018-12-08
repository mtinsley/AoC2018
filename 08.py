import sys
from collections import deque

meta_total = 0


def make_node():
    return {
        'children': [],
        'meta_data': [],
    }


def build_tree(data):
    global meta_total
    n = make_node()
    child_count = data.popleft()
    meta_count = data.popleft()
    for _ in range(child_count):
        n['children'].append(build_tree(data))
    for _ in range(meta_count):
        m = data.popleft()
        meta_total += m
        n['meta_data'].append(m)
    return n


def node_value(node):
    if len(node['children']) == 0:
        return sum(node['meta_data'])

    children = [node['children'][i - 1] for i in node['meta_data'] if 0 < i <= len(node['children'])]

    return sum(map(node_value, children))


sys.setrecursionlimit(10000)
inp = open('08.txt', 'r').read().strip()
root = build_tree(deque([int(n) for n in inp.split(' ')]))

print('Part One: {0}'.format(meta_total))
print('Part Two: {0}'.format(node_value(root)))
