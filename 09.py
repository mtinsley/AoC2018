from blist import *

MAX_MARBLE = 71646 * 100  # 71646 for part one, 71646 * 100 for part 2
PLAYER_COUNT = 412

players = {p: 0 for p in range(PLAYER_COUNT)}
player = 0
# Initialize the game state to the fourth turn to side step edge cases
marbles = blist([0, 2, 1, 3])  # Using blist for better list insert performance
curr = 3

# Start the game
for i in range(4, MAX_MARBLE):
    if i % 23 == 0:
        # Find the node 7 places counter-clockwise from the current node
        target = curr - 7
        if target < 0:
            target = len(marbles) - abs(curr - 7)
        # Update the player's score
        players[player] += (i + marbles[target])
        # Delete the target node
        del marbles[target]
        # Curr becomes the node that is now at the target position (ie the node after the node that was just deleted)
        curr = target
    else:
        # Insert a node between curr+1 and curr+2
        curr += 2
        if curr > len(marbles):
            curr = 1
        marbles.insert(curr, i)

    player += 1
    if player == len(players):
        player = 0

print(max(players.values()))
