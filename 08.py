import sys
from collections import deque

meta_total = 0


def make_node():
    return {
        'children': [],
        'meta_data': [],
    }


def build_tree(data):
    """
    Builds a tree from the given deque. Values are popped off of the deque as the tree is built.
    """
    global meta_total  # Keep a running total of the meta data values
    n = make_node()
    # The first and second values in data are the number of children for this node and the number of meta data entires respectively.
    child_count = data.popleft()
    meta_count = data.popleft()
    for _ in range(child_count):
        # Recursively build subtrees for each child
        n['children'].append(build_tree(data))
    for _ in range(meta_count):
        # Pop the meta data values off of the deque and update the total
        m = data.popleft()
        meta_total += m
        n['meta_data'].append(m)
    return n


def node_value(node):
    """
    Determine the value of the given node.
     - For nodes without children, the value is the sum of meta_data.
     - For nodes with children, the value is the sum of the values calculated for the children referenced in meta_data.
       Values in meta_data that are out of range are ignored.
    """
    if len(node['children']) == 0:
        return sum(node['meta_data'])
    # Find children referenced in meta_data
    children = [node['children'][i - 1] for i in node['meta_data'] if 0 < i <= len(node['children'])]
    # Recurse over children and return the sum of their values
    return sum(map(node_value, children))


sys.setrecursionlimit(10000)
inp = open('08.txt', 'r').read().strip()
root = build_tree(deque([int(n) for n in inp.split(' ')]))

print('Part One: {0}'.format(meta_total))
print('Part Two: {0}'.format(node_value(root)))
