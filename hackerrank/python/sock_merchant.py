#!/bin/python3

import sys


n = int(input().strip())
c = [int(c_temp) for c_temp in input().strip().split(' ')]

pairs = 0
singles = set()
for s in c:
    if s in singles:
        singles.remove(s)
        pairs += 1
    else:
        singles.add(s)
print(pairs)
