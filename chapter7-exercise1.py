#Amanda Thomas
#Chapter 7 Exercises
#Exercise 1
user_data = raw_input("Enter a file name: ")
lines_list = [line for line in open(user_data, 'r')]


def format_text(data):
    for line in lines_list:
        if line == "\n":
            pass
        print line.strip("\n").upper()

format_text(lines_list)