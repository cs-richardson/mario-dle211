"""
This program will create a half-pyramid based on the height given by the user.
Coded by Justin Le
"""

# Sets variable height to -1 so that the while loop below works upon
# initializing
height = -1

# Asks the user for an input until they input a number between 0 and 23 inclusive
while height < 0 or height > 23:
    height = int(input("Height: "))

# Creates a half-pyramid as tall as the user's input
if height != 0:
        line = " " * (height - 1)
        line = line + "##"
        print(line)
        for i in range(0, height - 1):
            line = line[1:]
            line = line + "#"
            print(line)
