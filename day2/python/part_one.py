#! /usr/bin/env python3

# find games that could have 12 red, 13 green, 14 blue
# add up the game IDS


class match():
    red = 0
    green = 0
    blue = 0

    def __init__(self, inputstr: str):
        id, sets = inputstr.split(":")
        self.id = id.split()[1]
        self.sets = [pulls.strip() for pulls in sets.split(";")]

        for colors in self.sets:
            color_groups = [color.strip() for color in colors.split(",")]
            print(color_groups)


test =  "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"

this = match(test)
color_str = "red"

print(this.__getattribute__(color_str))
