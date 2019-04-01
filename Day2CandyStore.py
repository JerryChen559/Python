
candyList = ["Snickers", "Kit Kat", "Sour Patch Kids", "Juicy Fruit",
             "Sweedish Fish", "Skittles", "Hershey Bar", "Skittles", "Starbursts", "M&Ms"]

allowance = 5

candyCart = []


for candy in candyList:
    print("[" + str(candyList.index(candy)) + "] " + candy)

print("Choose 5 candies.")
for x in range(allowance):
    selected_candy = input("Pick candy number " + str(x+1) + ": ")
    candyCart.append(candyList[int(selected_candy)])

print("Chosen list of candy: ")
for candy in candyCart:
    print(candy)
