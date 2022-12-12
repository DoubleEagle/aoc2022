input_file = open('day10_dummyinput.txt')
input_file = open('day10_input.txt')

instructions = input_file.read().split('\n')

cycle = 1
x = 1
signal_strengths = []
crt = []


def sprite_is_visible(cycle_num, sprite_middle):
    if abs(sprite_middle - (cycle_num-1) % 40) <= 1:
        return True
    return False


def pretty_print(to_print):
    for i in range(0, len(to_print), 40):
        for char in to_print[i:i + 40]:
            print(char, end="")
        print()


def print_line(x):
    for i in range(0, 40):
        if abs(x - i) <= 1:
            print("#", end="")
        else:
            print(".", end="")
    print("")


def add_crt_unit():
    global crt, cycle, x
    if sprite_is_visible(cycle, x):
        crt.append("#")
    else:
        crt.append(".")


for instruction in instructions:
    if instruction == "noop":
        add_crt_unit()
        # pretty_print(crt)
        cycle += 1
    elif instruction.startswith("addx"):
        value = int(instruction.split(" ")[1])
        for i in range(2):
            add_crt_unit()
            # pretty_print(crt)
            cycle += 1
            if cycle in [20, 60, 100, 140, 180, 220]:
                signal_strengths.append(x * cycle)
        # end of operation and cycles
        x += value

print("Part 1:", sum(signal_strengths))

print("Part 2:")
pretty_print(crt)
