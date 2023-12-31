#! /usr/bin/env python3

# find games that could have 12 red, 13 green, 14 blue
# add up the game IDS

class match():
    red = 0
    green = 0
    blue = 0

    def __init__(self, inputstr: str = "", bag_count: tuple[int, int, int] = (0,0,0)):
        if inputstr:
            self.set_input(inputstr)
        self.set_bagcount(*bag_count)

    def calculate(self):
        if self.set_strs is None:
            raise KeyError
        for i, colors in enumerate(self.set_strs):
            color_groups = [color.strip() for color in colors.split(",")]
            # print(color_groups)
            set = [0,0,0]
            for group in color_groups:
                if "red" in group:
                    set[0] = int(group.split()[0])
                if "green" in group:
                    set[1] = int(group.split()[0])
                if "blue" in group:
                    set[2] = int(group.split()[0])
            self.sets.append(set)
        # print(self.sets)

    def set_input(self, inputstr: str):
        id, sets = inputstr.split(":")
        self.id = int(id.split()[1])
        self.set_strs = [pulls.strip() for pulls in sets.split(";")]
        self.sets = []

    def set_bagcount(self, red: int, green: int, blue: int):
        self.red = red
        self.green = green
        self.blue = blue

    def check_if_possible(self):
        for set in self.sets:
            if set[0] > self.red or set[1] > self.green or set[2] > self.blue:
                return False
        return True

bag_count = (12, 13, 14)
matcher = match(bag_count=bag_count)

with open("input") as f:
    count = 0
    for line in f.readlines():
        # print(line.strip())
        matcher.set_input(line)
        matcher.calculate()
        if matcher.check_if_possible():
            count = count + matcher.id
    print(count)
