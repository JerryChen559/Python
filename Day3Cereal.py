# # Cereal Reader

# ## Instructions

# * Read through the csv of cereals.
# * Find all the cereals with 5 grams of fiber or more.
#   * Fiber is column H in your csv.
# * Print those out to your terminal

# ## Hint
# * Everything in the csv is stored as a string and certain rows have a decimal. How can we convert these to a float?

# ## Bonus
# * Try the following again but this time using the `cereal.csv` which has a header included in the file.

# -------------------------------------------------------------------
# regular solution

import os
import csv

cereal_csv = os.path.join("Resources", "cereal.csv")

with open(cereal_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    for row in csvreader:
        if float(row[7]) >= 5:
            print(row[0])


# -------------------------------------------------------------------
# bonus solution

cereal_csv_path = os.path.join("Resources",  "cereal_bonus.csv")

with open(cereal_csv_path, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')

    # skip the first row of the csv, skip the header data.
    next(csv_reader, None)

    for row in csv_reader:
        if float(row[7]) >= 5:
            print(row)
