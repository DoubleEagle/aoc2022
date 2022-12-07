# input_file = open('day7_dummyinput.txt')
input_file = open('day7_input.txt')

input = input_file.read().split('\n')

filesystem_tree = {'/': {}}
current_location = ['/']
all_sizes = []
sizes_under_100000 = []


def pretty_print_tree(tree, prefix=""):
    for key, value in tree.items():
        if type(value) is dict:
            print(prefix + "- " + key)
            pretty_print_tree(value, prefix + "\t")
        else:
            print(prefix + "- " + str(key) + " (size " + str(value) + ")")


def insert_directory(path, tree, dir_name):
    if len(path) <= 1:
        tree[path[0]][dir_name] = {}
        return tree
    for directory, contents in tree.items():
        if directory == path[0]:
            tree[directory] = insert_directory(path[1:], tree[directory], dir_name)
    return tree


def insert_file(path, tree, file_name, size):
    if len(path) <= 1:
        tree[path[0]][file_name] = int(size)
        return tree
    for directory, contents in tree.items():
        if directory == path[0]:
            tree[directory] = insert_file(path[1:], tree[directory], file_name, size)
    return tree


def parse_command(command, state, location):
    if command[:2] != "$ ":
        print("This is not a command!")
        exit()
    # if command == "$ ls":
    #     print("> reading directory \n")
    elif "$ cd " in command:
        # print("> change directory \n")
        new_location = command.split(" ")[2]
        if new_location == "..":
            location = location[:-1]
        else:
            # check if already in tree and if not add it
            state = insert_directory(location, state, new_location)
            # change location
            location.append(new_location)
    return state, location


def globally_calculate_directory_sizes(tree):
    global all_sizes
    size = 0
    for directory, contents in tree.items():
        if type(contents) is int:
            size += contents
        else:
            d_s = globally_calculate_directory_sizes(contents)
            size += d_s
            all_sizes.append(d_s)
            if d_s <= 100000:
                sizes_under_100000.append(d_s)
    return size


for line in input[1:]:
    if line.startswith("$ "):
        filesystem_tree, current_location = parse_command(line, filesystem_tree, current_location)
    elif line.startswith("dir "):
        # add directory under current directory
        insert_directory(current_location, filesystem_tree, line.split(' ')[1])
    elif line.split(" ")[0].isnumeric():
        size = line.split(" ")[0]
        file_name = line.split(" ")[1]
        filesystem_tree = insert_file(current_location, filesystem_tree, file_name, size)
    else:
        print("Something unparsable found:", line)
        exit()

pretty_print_tree(filesystem_tree)

total_size = globally_calculate_directory_sizes(filesystem_tree)

print("Part 1:", sum(sizes_under_100000))

# This is total beun, but at this point I was done with it
total_disk_space = 70000000
at_least_free = 30000000
max_size = total_disk_space - at_least_free

space_to_free = total_size - max_size

candidates = filter(lambda x: (x >= space_to_free), all_sizes)
print("Part 2:", min(list(candidates)))