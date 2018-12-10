def make_node(n):
    return {
        'value': n,
        'prev': None,
        'next': None,
    }

def seek(node, n):
    """
    Seeks to the node n places away from the given node. Negative n indicates prev (counter-clockwise) direction
    """
    direction = 'next' if n > 0 else 'prev'
    for _ in range(abs(n)):
        node = node[direction]

    return node

def play_turn(curr, node_value):
    if node_value % 23 == 0:
        # Seek to the node 7 places counter-clockwise from the current node
        curr = seek(curr, -7)
        # Remove the node by updating it's prev and next to point to one another
        next = curr['next']
        curr['prev']['next'] = next
        next['prev'] = curr['prev']
        # Compute the score and delete the removed node
        score = node_value + curr['value']
        del curr

        return next, score

    # Insert the new node between curr+1 and curr+2
    curr = seek(curr, 1)
    new_node = make_node(node_value)
    new_node['prev'] = curr
    new_node['next'] = curr['next']
    curr['next']['prev'] = new_node
    curr['next'] = new_node

    return new_node, 0


# Initialize Game
MAX_MARBLE = 71646 * 100  # 71646 for part one, 71646 * 100 for part 2
PLAYER_COUNT = 412

player_scores = [0 for _ in range(PLAYER_COUNT)]
curr_player = 0

curr = make_node(0)
curr['prev'] = curr
curr['next'] = curr

# Start Game
for i in range(1, MAX_MARBLE):
    curr, turn_score = play_turn(curr, i)
    player_scores[curr_player] += turn_score
    curr_player = curr_player + 1 if curr_player + 1 < len(player_scores) else 0

print(max(player_scores))
