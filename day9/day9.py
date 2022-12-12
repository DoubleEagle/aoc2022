input_file = open('day9_dummyinput.txt')
input_file = open('day9_input.txt')

lines = input_file.read().split('\n')

head_location = (0,0)
tail_location = (0,0)

seen_positions = set()


def tail_moves(head, tail):
    horizontal_dist = abs(head[0] - tail[0])
    vertical_dist = abs(head[1] - tail[1])

    # diagonal is close enough
    if horizontal_dist == 1 and vertical_dist == 1:
        return False
    # not diagonal, but 2 or more away
    if horizontal_dist + vertical_dist >= 2:
        return True
    # close enough to not move
    return False


def move_head(x, y, direction):
    match direction:
        case "R":
            # print('right')
            return x + 1, y
        case "U":
            # print('up')
            return x, y + 1
        case "L":
            # print('left')
            return x - 1, y
        case "D":
            # print('down')
            return x, y - 1
    print('Something when wrong!')
    exit()


def plus_or_minus(value1, value2):
    if value1 - value2 < 0:
        return -1
    elif value1 - value2 > 0:
        return 1


def move_tail(head, tail):
    horizontal_dist = abs(head[0] - tail[0])
    vertical_dist = abs(head[1] - tail[1])

    # diagonal is close enough
    if horizontal_dist == 1 and vertical_dist == 1:
        return tail
    # not diagonal, but 2 or more away
    if horizontal_dist + vertical_dist >= 2:
        if head[0] == tail[0]:
            # print('move on y axis only')
            return tail[0], tail[1] + plus_or_minus(head[1], tail[1])
        elif head[1] == tail[1]:
            # print('move on x axis only')
            return tail[0] + plus_or_minus(head[0], tail[0]), tail[1]
        else:
            # print('move one diagonal')
            return tail[0] + plus_or_minus(head[0], tail[0]), tail[1] + plus_or_minus(head[1], tail[1])
    # close enough to not move
    return tail


for line in lines:
    line_splitted = line.split(" ")
    direction = line_splitted[0]
    times = int(line_splitted[1])

    for i in range(times):
        head_location = move_head(head_location[0], head_location[1], direction)
        if tail_moves(head_location, tail_location):
            tail_location = move_tail(head_location, tail_location)
        seen_positions.add(tail_location)


print("Part 1:", len(seen_positions))


head_location = (0,0)
tail_locations = [(0,0)] * 9
seen_positions = set()

for line in lines:
    line_splitted = line.split(" ")
    direction = line_splitted[0]
    times = int(line_splitted[1])

    for i in range(times):
        # move head
        head_location = move_head(head_location[0], head_location[1], direction)

        # move each of subsequent tails
        # first tail:
        if tail_moves(head_location, tail_locations[0]):
            tail_locations[0] = move_tail(head_location, tail_locations[0])
            # all subsequent tails
            for tail_num in range(1, len(tail_locations)):
                if tail_moves(tail_locations[tail_num - 1], tail_locations[tail_num]):
                    tail_locations[tail_num] = move_tail(tail_locations[tail_num - 1], tail_locations[tail_num])
                else:
                    # if one part of the tail doesn't move, all subsequent tails don't
                    # move either, so we can just quit this loop
                    break
        # add last tail to seen positions
        seen_positions.add(tail_locations[-1])


print("Part 2:", len(seen_positions))
