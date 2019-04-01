# Quick lesson in python
# set correct python version: source activate PythonData
# run python program: python <file name>

firstName = input("Enter first name: ")
lastName = input("Enter last name: ")  # input
age = int(input("Enter age: "))  # int
trueFalse = bool(input("Enter any text if the statement is true "))  # bool

print("Your name is " + str(firstName) + " " + str(lastName))  # str
print("You are " + str(age) + " years old")  # concatenate
print("The summary above is " + str(trueFalse))  # output is True or False

x = 1  # variable
y = 10

if x < 10:  # do not need parentheses
    print("x is less than 2")
if (x == 1 and y == 10):  # and
    print("x is equal to 1 and y is equal to 10")
if x < 15 or y == 10:  # or
    print("or statement")


myList = [1, "meme", "lol", 8]  # list
myTuple = (1, "meme", 6, 5)  # tuple # immutable
print(len(myList))  # len
print(myTuple.index(5))  # index of something

myList.pop(0)  # pops specific index from list
print(myList)  # prints entire list


# for loops
for m in range(5):  # range 0 - 4
    print(m)
for p in range(2, 7):  # range 2 through 6
    print(p)

word = 'peace'
for letters in word:  # interate through letters in a string
    print(letters)

meal = ["noodles", 'cool-aid', 'fruit', 'pie']
for food in meal:  # interate food through meal array
    print(food)

# while loop
run = "y"

while run == "y":
    print("running!")
    run = input("Enter 'y' to run again!")  # condition to reenter loop.
