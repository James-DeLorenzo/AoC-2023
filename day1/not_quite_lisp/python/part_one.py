#! /usr/bin/env python3

floor = 0

with open("../input") as fin:
    for paren in fin.read():
        move = 1 if '(' == paren else -1 if ')' == paren else 0
        floor = floor + move
print(floor)
