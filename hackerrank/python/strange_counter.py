#!/bin/python3

import sys


t = int(input().strip())

curr_val = 3
count = curr_val
while curr_val < t:
    t -= curr_val
    curr_val *= 2
print(curr_val - t + 1)
