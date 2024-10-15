import random
from collections import deque

puzzle = [0, 1, 2, 3, 4, 5, 6, 7, 8]  # Initial puzzle state
empty_tile = 0  # Represents the blank tile

directions = {
    'up': -3,
    'down': 3,
    'left': -1,
    'right': 1
}

# Shuffle the puzzle
def shuffle():
    global puzzle, empty_tile
    for _ in range(100):
        random_direction = random.choice(list(directions.keys()))
        move_tile(random_direction)

# Update UI (simulated as printing the puzzle)
def update_ui():
    for i in range(0, 9, 3):
        print(puzzle[i:i+3])
    print()

# Move tile in the given direction
def move_tile(direction):
    global empty_tile
    target_index = puzzle.index(0) + directions[direction]

    if is_valid_move(target_index, direction):
        puzzle[empty_tile], puzzle[target_index] = puzzle[target_index], puzzle[empty_tile]
        empty_tile = target_index
        update_ui()

# Validate move based on boundaries and puzzle rules
def is_valid_move(target_index, direction):
    if target_index < 0 or target_index > 8:
        return False
    if (empty_tile % 3 == 0 and direction == 'left') or (empty_tile % 3 == 2 and direction == 'right'):
        return False
    return True

# BFS Algorithm
def bfs_solve():
    visited = set()
    queue = deque([{'state': puzzle[:], 'moves': []}])

    while queue:
        current = queue.popleft()
        state, moves = current['state'], current['moves']

        if is_goal(state):
            animate_moves(moves)
            return

        visited.add(tuple(state))

        for dir in directions.keys():
            new_state = move_state(state[:], dir)
            if new_state and tuple(new_state) not in visited:
                queue.append({'state': new_state, 'moves': moves + [dir]})

# Move state for BFS
def move_state(state, direction):
    empty_index = state.index(0)
    target_index = empty_index + directions[direction]

    if is_valid_move_bfs(empty_index, target_index, direction):
        state[empty_index], state[target_index] = state[target_index], state[empty_index]
        return state
    return None

# Validate move for BFS
def is_valid_move_bfs(empty_index, target_index, direction):
    if target_index < 0 or target_index > 8:
        return False
    if (empty_index % 3 == 0 and direction == 'left') or (empty_index % 3 == 2 and direction == 'right'):
        return False
    return True

# Check if current state matches the goal
def is_goal(state):
    return state == [0, 1, 2, 3, 4, 5, 6, 7, 8]

# Animate the solution moves
def animate_moves(moves):
    i = 0
    for move in moves:
        move_tile(move)

# Initialize puzzle on load
update_ui()
