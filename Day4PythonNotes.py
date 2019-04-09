# formatted string

first = 'John'
last = 'Smith'

message = f'{first} {last} is a coder.'
print(message)

# methods for strings
print(message.upper())
# also can use .find('S') and .replace('Smith','Rocks')

# bool
print('n' in message)

# ----------------------------------------------
# arithmetic operations
# +: add or concatinate
# / divide
# // divide integer
# ** power

# math module
#abs, round
# math.floor, math.ceil

# Side note: while loops can also have else statements

numbers = [5, 2, 5, 2, 2]

for number in numbers:
    print('x'*number)

# same outcome. practice with inner loop
for num in numbers:
    output = ''
    for x in range(num):
        output += 'y'
    print(output)
