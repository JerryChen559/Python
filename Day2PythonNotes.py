# Import File

import random
import string  # all imports at the top

print(string.ascii_letters)

for x in range(8):  # iterate from index 0 through 7
    print(random.randint(3, 20))  # random numbers from 3-20


# ------------------------------------------------------------------

# Read File

# Old way to open CSV
# file = 'Resources/input.txt'  # store file path associated with file

# with open(file, 'r') as text:  # r is read
#     print(text)

#     lines = text.read()  # store text in a variable called lines
#     print(lines)

# Correct way to open CSV
# import csv
# import os
# csvpath = os.path.join("Resources", "netflix_ratings.csv")
# with open(csvpath, newline="") as csvfile:
#     csvreader = csv.reader(csvfile, delimiter=",")
#     print(csvreader)
#     for row in csvreader:
#         print(row)

# ------------------------------------------------------------------

# Write File

# import csv
# import os

# # Specify the file to write to
# output_path = os.path.join('output', 'new.csv')

# # Open the file using "write" mode. Specify the variable to hold the contents
# with open(output_path, 'w', newline='') as csvfile:

#     # Initialize csv.writer
#     csvwriter = csv.writer(csvfile, delimiter=',')

#     # Write the first row (column headers)
#     csvwriter.writerow(['First Name', 'Last Name', 'SSN'])

#     # Write the second row
#     csvwriter.writerow(['Caleb', 'Frost', '505-80-2901'])

# ------------------------------------------------------------------

# Zipping lists

# Three Lists
indexes = [1, 2, 3, 4]
employees = ["Michael", "Dwight", "Meredith", "Kelly"]
department = ["Boss", "Sales", "Sales", "HR"]

# Zip all 3 lists together into tuples(immutable)
roster = zip(indexes, employees, department)

# print contents of each row.
for employee in roster:
    print(employee)

# (1, 'Michael', 'Boss')
# (2, 'Dwight', 'Sales')
# (3, 'Meredith', 'Sales')
# (4, 'Kelly', 'HR')

# ------------------------------------------------------------------

# Functions

# Defining arrays
listOne = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
listTwo = [11, 12, 13, 14, 15]

# Defining functions


def listInformation(simpleList):
    print("The values within the list are...")
    for value in simpleList:
        print(value)
    print("The length of this list is... " + str(len(simpleList)))


# Calling functions
listInformation(listOne)
listInformation(listTwo)
