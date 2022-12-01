input_file = open('day1_input.txt')

result = []

for elf in input_file.read().split('\n\n'):
    calories = elf.split('\n')
    
    sum_c = 0
    for c in calories:
        sum_c += int(c)
    result.append(calories)

print(sum(sorted(result)[-3:]))