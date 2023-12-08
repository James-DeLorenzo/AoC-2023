#! /usr/bin/env python3

floor = 0

with open("../input") as fin:
    line = fin.read()
    for i, paren in enumerate(line):
        move = 1 if '(' == paren else -1 if ')' == paren else 0
        floor = floor + move
        if floor < 0:
            print(i+1)
            break
