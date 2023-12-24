#! /usr/bin/env python3

# find min num of dice for each game
# add up the game dice amount multiplied together

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
        for colors in self.set_strs:
            color_groups = [color.strip() for color in colors.split(",")]
            # print(color_groups)
            for group in color_groups:
                if "red" in group:
                    red = int(group.split()[0])
                    self.red = max(self.red, red)
                if "green" in group:
                    green = int(group.split()[0])
                    self.green = max(self.green, green)
                if "blue" in group:
                    blue = int(group.split()[0])
                    self.blue = max(self.blue, blue)
            # print(f"{self.red} {self.green} {self.blue}")

    def set_input(self, inputstr: str):
        id, sets = inputstr.split(":")
        self.id = int(id.split()[1])
        self.set_strs = [pulls.strip() for pulls in sets.split(";")]
        self.sets = []
        self.set_bagcount(0,0,0)

    def set_bagcount(self, red: int, green: int, blue: int):
        self.red = red
        self.green = green
        self.blue = blue

    def check_if_possible(self):
        for set in self.sets:
            if set[0] > self.red or set[1] > self.green or set[2] > self.blue:
                return False
        return True

    def get_prod(self):
        prod = self.red * self.green * self.blue
        # print(f"game {self.id} product: {prod}")
        return prod

matcher = match()

with open("input") as f:
    count = 0
    for line in f.readlines():
        # print(line.strip())
        matcher.set_input(line)
        matcher.calculate()
        if matcher.check_if_possible():
            count = count + matcher.get_prod()
    print(count)
