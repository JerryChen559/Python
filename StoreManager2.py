# Store Manager
# Redo Store Manager 1 with import

import os
import csv

store_csv = os.path.join("Resources", "store_items.csv")

with open(store_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    myList = list(csvreader)
    print(myList)

manage_system = "y"

# Run the code so long as the user wants to manage the systm
while manage_system == "y":

    # Take users input
    action_item = input(
        "What would like to do today? (a)dd new item, (r)emove an item, or (s)how all items ")

    # add item to dictionary
    if action_item == "a":

        item_added = input("What would you like to add? ")
        amount_added = input("How many would you like to add? ")

        myList.append([item_added, amount_added])

        print(item_added + " " + amount_added + " added!")

    # remove item
    elif action_item == "r":

        item_removed = input("Which item would you like to be removed? ")

        for x in myList:
            if item_removed in x[0]:
                myList.remove(x)

                print(item_removed + " has been removed! ")

        else:
            print("That item does not exist")

    # show all
    elif action_item == "s":

        print("Store inventory")
        print("----------")

        for key, value in myList:
            print(key + ": " + str(value))
            print("----------")

    else:
        print("Sorry the action is not available")

    # Check if the user wants to continue working within the system
    manage_system = input("Would you like to continue working? (y)es or (n)o ")
