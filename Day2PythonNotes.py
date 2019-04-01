# Import File
import random
import string  # all imports at the top

print(string.ascii_letters)

for x in range(8):  # iterate from index 0 through 7
    print(random.randint(3, 20))  # random numbers from 3-20


# ------------------------------------------------------------------

# Read File

file = 'Resources/input.txt'  # store file path associated with file

with open(file, 'r') as text:  # r is read
    print(text)

    lines = text.read()  # store text in a variable called lines
    print(lines)

# ------------------------------------------------------------------


# ------------------------------------------------------------------
# ------------------------------------------------------------------
