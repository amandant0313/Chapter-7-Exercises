#Amanda Thomas
#Chapter 7 Exercises
#Exercise 1
import sys

user_data = raw_input("Enter the file name: ")

if user_data == "na na boo boo":
    print "NA NA BOO BOO TO YOU - You have been punk'd!"
    sys.exit(0)

try:
    user_file = open(user_data, 'r')
except:
    print "File cannot be opened: " + user_data
    sys.exit(1)


lines_list = [line.strip("\n") for line in user_file]


def count_subject_lines(data):
    subject_count = 0
    for line in lines_list:
        if line.startswith("Subject"):
            subject_count += 1
    print subject_count

count_subject_lines(lines_list)