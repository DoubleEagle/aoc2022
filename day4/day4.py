import re

input_file = open('day4_dummyinput.txt')
input_file = open('day4_input.txt')

lines = input_file.read().split('\n')


def split_ranges(ranges_line):
    ranges = re.split(',|-', ranges_line)
    # print(ranges)
    return int(ranges[0]), int(ranges[1]), int(ranges[2]), int(ranges[3])


counter_1 = 0
counter_2 = 0

for line in lines:
    r1, r2, r3, r4 = split_ranges(line)
    if (r1 <= r3 and r2 >= r4) or (r1 >= r3 and r2 <= r4):
        counter_1 += 1
    if not (r2 < r3 or r4 < r1):
        counter_2 += 1
    # print(ranges)

print("Part 1:", counter_1)
print("Part 2:", counter_2)
