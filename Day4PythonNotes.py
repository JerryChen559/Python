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

# for loop
numbers = [5, 2, 5, 2, 2]

for number in numbers:
    print('x'*number)

# same outcome. practice with inner loop
for num in numbers:
    output = ''
    for x in range(num):
        output += 'y'
    print(output)


# max number
numnum = [4, 9, 2, 4, 5]
max = numnum[0]


for n in numnum:
    if n > max:
        max = n
print(max)


# ----------------------------------------------
# 2D lists => data science and Machine Learning
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix[0][2])  # => 3

# list methods (aka list functions)
# .append(obj) to end
# .insert(ind, obj) at beginning
# .remove(obj)
# .index(obj)
# .count(obj)
# .sort()
# .reverse()
# .copy()
# .pop(obj) => remove last item
# .clear() => empty list


nums_list = [2, 4, 2, 7, 6, 4, 9]
unique_list = []

# remove numbers with duplicates
for number in nums_list:
    if nums_list.count(number) == 1:
        unique_list.append(number)
print(unique_list)

# filter out duplicates
for number in nums_list:
    # if nums_list.count(number) > 1:
    if number not in unique_list:
        unique_list.append(number)
print(unique_list)


# tuples
# use () instead of []
# only two methods: count and index


# unpacking
coordinates = (1, 2, 3)
# unpack a list or tuple
# behind the scenes
# x = coordinates[0]
# y = coordinates[1]
# z = coordinates[2]
x, y, z = coordinates
print(x, y, z)

# dictionaries
# storing information as key value pairs
# left side is always a unique.
user = {
    "name": "Jerry",
    "age": 29,
    "city": "bean town"
}
print(user["name"])
print(user.get("name"))
# adding to a dictionary. just define it.
user["birthdate"] = "Jan 1, 2000"
print(user)

# dictionary exercise
digits_mapping = {
    "1": "one",
    "2": "two",
    "3": "three"
}

phone = "321"
output = ""
for digits in phone:
    output += digits_mapping.get(digits, '!') + " "
print(output)
