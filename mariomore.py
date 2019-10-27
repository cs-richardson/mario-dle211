"""
This program will create a pyramid with a gap in the middle based on the
height given by the user.
Coded by Justin Le
"""

# Sets variable height to -1 so that the while loop below works upon
# initializing
height = -1

# Asks the user for an input until they input a number between 0 and 23
while height < 0 or height > 23:
    height = int(input("Height: "))

# Creates a pyramid as tall as the user's input, with a gap in the middle
if height != 0:
    lineleft = " " * (height - 1)
    lineleft = lineleft + "#"
    lineright = "#"
    lineright = lineright + (" " * (height - 1))
    print(lineleft + "  " + lineright)
    for i in range(0, height - 1):
        lineleft = lineleft[1:]
        lineleft = lineleft + "#"
        lineright = lineright[0:(height - 1)]
        lineright = "#" + lineright
        print(lineleft + "  " + lineright)


