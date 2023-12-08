#! /usr/bin/env python3

total = 0
with open("../input") as fin:
    for data in fin.readlines():
        print(data.strip())
        nums = [d for d in data if d.isnumeric()]
        print(nums)
        total = total + int(''.join([nums[0], nums[-1]]))
        print(total)
# print(total)
