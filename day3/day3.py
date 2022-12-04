input_file = open('day3_dummyinput.txt')
input_file = open('day3_input.txt')

input = input_file.read().split('\n')
print(input)


def halves(input_string):
    return input_string[0:len(input_string)//2], input_string[len(input_string)//2:]


def common_letter(first, second, third=None):
    # print(first, second)
    first = set(list(first))
    second = set(list(second))
    if third is None:
        return first.intersection(second).pop()
    else:
        third = set(list(third))
        return first.intersection(second).intersection(third).pop()


def get_priority(letter):
    if letter.isupper():
        return ord(letter)-64+26
    else:
        return ord(letter)-96


result = 0

for line in input:
    first_half, second_half = halves(line)
    letter = common_letter(first_half, second_half)
    # print(letter, get_priority(letter))
    result += get_priority(letter)

print("Part 1:", result)


result_2 = 0

for i in range(0, len(input), 3):
    # for j in range(3):
    #     index = i * 3 + j
    # base_index =
    if i + 3 > len(input):
        break
    result_2 += get_priority(common_letter(input[i], input[i + 1], input[i + 2]))
    # print(input[index])

print("Part 2:", result_2)