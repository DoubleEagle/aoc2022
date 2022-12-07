input_file = open('day7_dummyinput.txt')
# input_file = open('day7_input.txt')

input = input_file.read().split('\n')

filesystem_tree = {'/': {}}
current_location = ['/']


def pretty_print_tree(tree, prefix="\t"):
    # print("=== pretty print", tree, prefix)
    for key, value in tree.items():
        if type(value) is dict:
            print(prefix + "- " + key)
            pretty_print_tree(value, prefix + "\t")
        else:
            print(prefix + "- " + str(key) + " (size " + str(value) + ")")


def find_current_directory_contents(location, tree):
    # print("=== finding directory...", location, tree)
    if len(location) > 1:
        return find_current_directory_contents(location[1:], tree[location[0]])
    else:
        # print("returning tree... ", tree)
        return tree[location[0]]


def add_to_tree(location, tree):
    if len(location) > 1:
        return add_to_tree(location[1:], tree[location[0]])
    else:
        return


def parse_command(command, state, location):
    if command[:2] != "$ ":
        print("This is not a command!")
        exit()
    if command == "$ ls":
        print("> reading directory \n")
    elif "$ cd " in command:
        print("> change directory \n")
        new_location = command.split(" ")[2]
        if new_location == "..":
            location = location[:-1]
        else:
            # change location
            location.append(new_location)
            # check if already in tree and if not add it
            state


for line in input:
    # print(line)
    if line.startswith("$ "):
        print("Command found:", line)
        filesystem_tree, current_location = parse_command(line, filesystem_tree, current_location)
    elif line.startswith("dir "):
        # add directory under current directory
        print("Directory found:", line)
    elif line.split(" ")[0].isnumeric():
        print("File found:", line)
    else:
        print("Something unparsable found:", line)
        exit()


test_tree = {'/': {'a': {'e': {'i': 120}}, 'b': 14848514, 'c': 14848514, 'd': {'j': 4060174}}}
# pretty_print_tree(test_tree)
print(find_current_directory_contents(['/', 'a', 'e'], test_tree))