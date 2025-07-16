# Madlibs game
# by filliing in blanks with random words

print("Welcome to MadLibs Game!")
print("Please provide the following words:\n")

# Collecting words from the user
noun = input("Enter a noun: ")
verb = input("Enter a verb: ")
adjective = input("Enter an adjective: ")
place = input("Enter a place: ")

# Creating the story with blanks filled in
story = f"""
Once upon a time, in a place called {place}, there was a very {adjective} {noun}.
Every day, it would {verb} happily through the fields.
Everyone in {place} loved the {noun} for its energy and charm.
"""

# Displaying the final story
print("\nHere is your MadLibs story:\n")
print(story)
