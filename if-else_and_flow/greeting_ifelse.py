#!/usr/bin/env python3

"""Greetings based on input"""

# User Input
print("Enter 1 or 2: ")
userInput = int(input(">"))

# Determine the appropriate response
if userInput == 1:
    print("Hello")
elif userInput == 2:
    print("Howdy")
else:
    print("Greetings!")
