# [file path to file] [mode]
# r - read
# w - write
# a - append
# r+ - read and write

employee_file = open("names.txt", "r")
for employee in employee_file.readlines():
    for letter in employee:
        print(letter)

#print(employee_file.readlines())

employee_file = open("names.txt", "a")
names = ["Mike", "Julia", "Thomas"]
for idx in range(len(names)):
    employee_file.write("\n" + names[idx] + " - Human Resources")

employee_file.close()
