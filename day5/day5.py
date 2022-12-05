import re

input_file = open('day5_dummyinput.txt')
input_file = open('day5_input.txt')

input = input_file.read()


def state_parser(state_input):
    lines = state_input.split("\n")[:-1]
    columns_num = (len(lines[-1]) + 1) // 4
    rows_num = len(lines)
    state = [[] for i in range(columns_num)]

    for row in range(rows_num - 1, 0 - 1, -1):
        for col in range(0, columns_num):
            x_index = col * 4 + 1
            if x_index >= len(lines[row]):
                continue
            if lines[row][x_index] == " ":
                continue
            state[col].append(lines[row][x_index])

    return state


def move_9000(how_many, from_col, to_col, state):
    for i in range(how_many):
        element = state[from_col - 1].pop()
        state[to_col - 1].append(element)
    return state


def move_9001(how_many, from_col, to_col, state):
    # fix column indexing
    from_col = from_col - 1
    to_col = to_col - 1

    if len(state[from_col]) == how_many:
        # print("move all")
        state[to_col].extend(state[from_col])
        state[from_col] = []
    else:
        # print("move part")
        to_move = state[from_col][-how_many:]
        state[from_col] = state[from_col][:-how_many]
        state[to_col].extend(to_move)

    return state


def parse_instruction(instruction):
    numbers = re.findall("[0-9]+", instruction)
    numbers = [int(i) for i in numbers]
    return numbers[0], numbers[1], numbers[2]


def get_top_crates(state):
    result = ""
    for stack in state:
        result += stack.pop()
    return result


state_input, instructions = input.split("\n\n")

state = state_parser(state_input)

for line in instructions.split("\n"):
    how_many, from_col, to_col = parse_instruction(line)
    state = move_9000(how_many, from_col, to_col, state)

print("Part 1:", get_top_crates(state))


state = state_parser(state_input)

for line in instructions.split("\n"):
    how_many, from_col, to_col = parse_instruction(line)
    state = move_9001(how_many, from_col, to_col, state)

print("Part 2:", get_top_crates(state))