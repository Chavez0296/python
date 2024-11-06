from collections import defaultdict, deque
import copy
import time

# Priority Queue for the open list
class PQ:
    def __init__(self):
        self.data = [None] * 5001
        self.data[4999] = 0
        self.data[5000] = 100000

    def add(self, my_path, new_cost):
        self.data[4999] += 1
        self.data[5000] = min(self.data[5000], new_cost)
        if not self.data[new_cost]:
            self.data[new_cost] = []
        self.data[new_cost].append(my_path)

    def lowest_cost(self, start):
        if self.data[4999] == 0:
            return 100000
        else:
            i = start
            while not self.data[i]:
                i += 1
            return i

    def remove(self):
        old_cost = self.data[5000]
        if self.data[4999] == 0:
            return None
        ans = self.data[old_cost].pop(0)
        self.data[4999] -= 1
        self.data[5000] = self.lowest_cost(old_cost)
        return ans

    def peek(self):
        old_cost = self.data[5000]
        return None if self.data[4999] == 0 else self.data[old_cost][0]

    def empty(self):
        return self.data[4999] == 0

# Hash table for the closed list
class MyHT:
    def __init__(self, size):
        self.size = size
        self.data = defaultdict(list)

    def hash_fn(self, s):
        def hash_helper(start, l):
            return start if not l else hash_helper(l[0] + start * 65559, l[1:])
        
        ans = 0
        for item in s:
            ans = hash_helper(ans, item)
        return ans

    def remove(self, key):
        hash_val = self.hash_fn(key) % self.size
        self.data[hash_val] = [kv for kv in self.data[hash_val] if kv[0] != key]

    def add(self, key, value):
        hash_val = self.hash_fn(key) % self.size
        self.data[hash_val].append((key, value))

    def get(self, key):
        hash_val = self.hash_fn(key) % self.size
        for k, v in self.data[hash_val]:
            if k == key:
                return v
        return None

# A* implementation
class MyPath:
    def __init__(self, state, previous=None, cost_so_far=0, total_cost=0):
        self.state = state
        self.previous = previous
        self.cost_so_far = cost_so_far
        self.total_cost = total_cost

    def states(self):
        if not self:
            return []
        return [self.state] + MyPath.states(self.previous)

expanded = 0
generated = 1

def astar(start_state, goal_p, successors, cost_fn, remaining_cost_fn):
    global expanded, generated
    expanded, generated = 0, 1
    open_list = PQ()
    closed_list = MyHT(1000000)
    open_list.add(MyPath(start_state), 0)
    while not open_list.empty():
        if goal_p(open_list.peek().state):
            return list(reversed(MyPath.states(open_list.peek())))
        my_path = open_list.remove()
        state = my_path.state
        new_val = my_path.total_cost
        hash_val = closed_list.hash_fn(state)
        closed_val = closed_list.get(state)
        if not closed_val or new_val < closed_val:
            expanded += 1
            if closed_val:
                closed_list.remove(state)
            closed_list.add(state, new_val)
            for state2 in successors(state):
                cost = my_path.cost_so_far + cost_fn(state,state2)
                cost2 = remaining_cost_fn(state2)
                total_cost = cost + cost2
                generated += 1
                open_list.add(MyPath(state2, my_path, cost, total_cost), total_cost)

# The rest of the code for testing and other purposes would go here

def costfn(state,state2):
    return 1

# Goal test function
def goal_test(state):
    for row in state:
        for square in row:
            if square == 2:  # box not on a goal
                return False
    return True

# Helper functions
def get_square(state, r, c):
    """Retrieve the content of a specific square in the grid, defaulting to a wall if out of bounds."""
    if 0 <= r < len(state) and 0 <= c < len(state[0]):
        return state[r][c]
    return 1  # Wall by default if out of bounds

def set_square(state, r, c, value):
    """Creates a new state with an updated square at a specific location."""
    new_state = copy.deepcopy(state)
    new_state[r][c] = value
    return new_state

def find_keeper(state):
    for row in range(len(state)):
        for col in range(len(state[row])):
            if state[row][col] == 3 or state[row][col] == 6:  # Assuming 3 is the keeper and 6 is the keeper on a goal
                return row, col
    return None  # Return None if the keeper is not found

def is_within_bounds(state, row, col):
    return 0 <= row < len(state) and 0 <= col < len(state[row])

def copy_state(state):
    return [row[:] for row in state]

def try_move(state, direction):
    # Locate the keeper
    keeper_row, keeper_col = find_keeper(state)

    # Direction offsets
    direction_offsets = {
        "up": (-1, 0),
        "down": (1, 0),
        "left": (0, -1),
        "right": (0, 1)
    }

    if direction not in direction_offsets:
        return None  # Invalid direction

    # Calculate new positions
    row_offset, col_offset = direction_offsets[direction]
    new_keeper_row, new_keeper_col = keeper_row + row_offset, keeper_col + col_offset
    beyond_row, beyond_col = new_keeper_row + row_offset, new_keeper_col + col_offset

    # Check if the target position is within bounds
    if not is_within_bounds(state, new_keeper_row, new_keeper_col):
        return None

    # Create a copy of the state for the new move
    new_state = copy_state(state)

    # Retrieve the target cell content
    target_cell = state[new_keeper_row][new_keeper_col]

    # Move logic for one box
    if target_cell == 0 or target_cell == 4:  # Blank or goal
        # Update keeper's previous cell
        new_state[keeper_row][keeper_col] = 4 if state[keeper_row][keeper_col] == 6 else 0
        # Move keeper to the new cell
        new_state[new_keeper_row][new_keeper_col] = 6 if target_cell == 4 else 3

    elif target_cell in {2, 5}:  # Box or box on goal
        # Check beyond cell (where box will be pushed)
        if not is_within_bounds(state, beyond_row, beyond_col):
            return None
        beyond_cell = state[beyond_row][beyond_col]

        # Validate push for one box
        if beyond_cell in {0, 4}:  # Can push box to blank or goal
            # Update keeper's previous cell
            new_state[keeper_row][keeper_col] = 4 if state[keeper_row][keeper_col] == 6 else 0
            # Move keeper to box's position
            new_state[new_keeper_row][new_keeper_col] = 6 if target_cell == 5 else 3
            # Move box to the beyond cell
            new_state[beyond_row][beyond_col] = 5 if beyond_cell == 4 else 2
            
            # Check for another box in the same direction
            second_box_row = beyond_row + row_offset
            second_box_col = beyond_col + col_offset
            
            # If a second box is present in the same direction
            if is_within_bounds(state, second_box_row, second_box_col):
                second_box_cell = state[second_box_row][second_box_col]
                if second_box_cell in {2, 5}:  # If the second box is also a box
                    beyond_second_row = second_box_row + row_offset
                    beyond_second_col = second_box_col + col_offset
                    
                    # Validate push for the second box
                    if is_within_bounds(state, beyond_second_row, beyond_second_col):
                        beyond_second_cell = state[beyond_second_row][beyond_second_col]
                        if beyond_second_cell in {0, 4}:  # Can push second box to blank or goal
                            # Move the second box
                            new_state[beyond_second_row][beyond_second_col] = 5 if beyond_second_cell == 4 else 2
                        else:
                            return None  # Can't push the second box
                    else:
                        return None  # Beyond second box is out of bounds

    else:
        return None  # Move is blocked

    return new_state


# Next states function
def next_states(state):
    """Generates all valid next states from the current state by moving the keeper."""
    directions = ['up', 'down', 'left', 'right']
    next_states_list = []

    for direction in directions:
        new_state = try_move(state, direction)
        if new_state is not None:
            next_states_list.append(new_state)
    
    return next_states_list

# Heuristic functions
def h0(state):
    """Trivial heuristic that returns 0."""
    return 0

def h1(state):
    """Counts boxes not on goal positions."""
    count = 0
    for row in state:
        for square in row:
            if square == 2:  # box not on goal
                count += 1
    return count
# This is admissible because it never overestimates the actual distance.

def hUID(state):
    boxes = [(r, c) for r in range(len(state)) for c in range(len(state[0])) if state[r][c] == 2]
    goals = [(r, c) for r in range(len(state)) for c in range(len(state[0])) if state[r][c] in [4, 5]]
    
    # Ensure goals are not empty to avoid ValueError
    if not goals:
        return 0
    
    # Manhattan distance heuristic: minimum distance from each box to any goal
    total_distance = sum(
        min(abs(box[0] - goal[0]) + abs(box[1] - goal[1]) for goal in goals) for box in boxes
    )
    
    return int(total_distance)  # Ensure integer return value


def print_state(state):
    # Mapping from integer values to their ASCII representation
    symbols = {
        0: ' ',
        1: '#',
        2: '$',
        3: '@',
        4: '.',
        5: '*',
        6: '+'
    }
    
    # Convert each row in the state to a string and print it
    for row in state:
        row_str = ''.join(symbols[cell] for cell in row)
        print(row_str)
    print()  # Blank line after each state for readability



initial_state = [
    [0, 0, 1, 1, 1, 1, 0, 0, 0],
    [1, 1, 1, 0, 0, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 2, 0, 1],
    [1, 0, 1, 0, 0, 1, 2, 0, 1],
    [1, 0, 4, 0, 4, 1, 3, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1]
]

# Running the A* algorithm
start_time = time.time()
solution_path = astar(initial_state, goal_test, next_states, costfn, hUID)
print("%s seconds" % (time.time() - start_time))

count = 0

if solution_path:
    print("Solution found with the following states:")
    for state in solution_path:
        count += 1
        print(f"State #: {count}\n")
        print_state(state)
else:
    print("No solution exists.")
