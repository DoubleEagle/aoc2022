import numpy as np

input = open("day8_dummyinput.txt", 'r').read()
input = open("day8_input.txt", 'r').read()

grid = np.array([[int(x) for x in list(y)] for y in input.split("\n")])


def visible_in_line(line, index):
    value = line[index]
    if max(line[:index + 1]) == value and np.count_nonzero(line[:index + 1] == value) == 1:
        return True
    if max(line[index:]) == value and np.count_nonzero(line[index:] == value) == 1:
        return True
    return False


def is_visible(row, col):
    global grid
    if row == 0 or col == 0 or row == len(grid) - 1 or col == len(grid[0]) - 1:
        return True
    # check horizontal
    if visible_in_line(grid[row, :], col):
        return True
    # check vertical
    if visible_in_line(grid[:, col], row):
        return True
    return False


def scenic_score(row, col):
    # print("=============Calculating scenic score")
    scores = []
    value = grid[row][col]
    # left
    left_trees = grid[row][:col][::-1]
    # print('left', left_trees)
    scores.append(score_per_side(left_trees, value))
    # top
    top_trees = grid[:, col][:row][::-1]
    # print('top', top_trees)
    scores.append(score_per_side(top_trees, value))
    # right
    right_trees = grid[row][col + 1:]
    # print('right', right_trees)
    scores.append(score_per_side(right_trees, value))
    # bottom
    bottom_trees = grid[:, col][row + 1:]
    # print('bottom', bottom_trees)
    scores.append(score_per_side(bottom_trees, value))
    # print((row, col, value), scores, np.prod(scores))
    return np.prod(scores)


def score_per_side(line, value):
    seen_trees = 0
    for tree in line:
        seen_trees += 1
        if tree >= value:
            # bonk
            return seen_trees
    return seen_trees


visible_counter = 2 * len(grid) + 2 * (len(grid[0]) - 2)
scenic_scores = []

for row in range(1, len(grid) - 1):
    for col in range(1, len(grid[0]) - 1):
        if is_visible(row, col):
            visible_counter += 1
        scenic_scores.append(scenic_score(row, col))


print("Part 1:", visible_counter)

# print(grid)

print("Part 2:", max(scenic_scores))