input_file = open('day2_input.txt')

plays = input_file.read().split('\n')

print(plays)


def get_shape_score(shape):
    if shape == "A" or shape == "X":
        return 1
    elif shape == "B" or shape == "Y":
        return 2
    else:
        return 3


def get_outcome(shape1, shape2):
    if shape1 == "A":
        if shape2 == "X":
            return 3
        elif shape2 == "Y":
            return 6
        else:
            return 0
    if shape1 == "B":
        if shape2 == "X":
            return 0
        elif shape2 == "Y":
            return 3
        else:
            return 6
    if shape1 == "C":
        if shape2 == "X":
            return 6
        elif shape2 == "Y":
            return 0
        else:
            return 3


def get_play(shape1, win):
    if shape1 == "A":
        if win == "X":
            return 0, "Z"
        elif win == "Y":
            return 3, "X"
        else:
            return 6, "Y"
    if shape1 == "B":
        if win == "X":
            return 0, "X"
        elif win == "Y":
            return 3, "Y"
        else:
            return 6, "Z"
    if shape1 == "C":
        if win == "X":
            return 0, "Y"
        elif win == "Y":
            return 3, "Z"
        else:
            return 6, "X"


total_score = 0

for play in plays:
    shape1, shape2 = play.split(" ")
    # total_score += get_shape_score(shape2)
    # total_score += get_outcome(shape1, shape2)

    # result = get_play(shape1, shape2)
    # print(result)
    points, played = get_play(shape1, shape2)

    total_score += get_shape_score(played)
    total_score += points

print(total_score)
