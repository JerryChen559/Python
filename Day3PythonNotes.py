# # git commands review
# git clone < repo_name >  # branch off master
# # code your changes
# git status  # see which files have not yet been commited.
# git add .  # add all files
# git commit - m "message for you and other devs to read in the future"  # commit code
# git - am "message"  # add all files and commits
# git status  # check status again before pushing
# git push origin master  # push code to master

# ------------------------------------------------------------
# dictionary
# anouther commonly used datatype
# key value pair
# keys are always strings. values can be anything

# A dictionary can contain multiple types of information
another_actor = {"name": "Sylvester Stallone", "age": 62,
                 "married": True, "best movies": ["Rocky", "Rocky 2", "Rocky 3"]}
print(another_actor["name"] + " was in  " + another_actor["best movies"][0])
# you can prevent key error with .get(). You can all a fail safe as a 2nd argument.
# handy for data with missing values.
is_married = another_actor.get("married", False)

# ------------------------------------------------------------

# Two Dictionaries
actress = {"name": "Angelina Jolie",
           "genre": "Action", "nationality": "United States"}
actor = {"name": "Adam Sandler", "genre": "comedy",
         "nationality": "United States"}

# Access all the keys
print(actor.keys())

# Access all values
print(actress.values())

# We can iterate through dictionaries with a for-loop
for key in actress.keys():
    print("This is a key:", key)

# Looping through values
for value in actress.values():
    print("This is a value:", value)

# Use items() to loop through both keys and values
# this is called unpacking items in python
for key, value in actress.items():
    print("This is a key:", key)
    print("This is a value:", value)

# ---------------------------------------------------------------
film = {"title": "Interstellar", "revenues": {
    "United States": 360, "China": 250, "United Kingdom": 73}}
# Use del to delete a key-value pair from a dictionary
del film["revenues"]
print(film)

# ---------------------------------------------------------------

# Add a key-value pair to a dictionary
actor["hair"] = "brown"
actor["genre"] = "drama"
print(actor)
