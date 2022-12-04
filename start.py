import os
import shutil

print("Enter day number:")

day_num = str(input())

print("Creating files for day ", day_num, "...")

os.mkdir("day" + day_num)

f = open("day" + day_num + "/day" + day_num + ".py", "a")
f.write("input_file = open('day" + day_num + "_dummyinput.txt')\n"
        "# input_file = open('day" + day_num + "_input.txt')\n"
        "\n"
        "input = input_file.read().split('\\n')")
f.close()

f_dummy = open("day" + day_num + "/day" + day_num + "_dummyinput.txt", "a")
f_dummy.close()

f_input = open("day" + day_num + "/day" + day_num + "_input.txt", "a")
f_input.close()