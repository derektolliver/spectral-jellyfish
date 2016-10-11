#!/bin/python3

import sys


n = int(input().strip())
c = [int(c_temp) for c_temp in input().strip().split(' ')]

count = 0
cloud = 0
while cloud < len(c) - 1:
    count += 1
    if cloud + 2 <= len(c) - 1 and c[cloud] == 0:
        cloud = cloud + 2
    else:
        cloud = cloud + 1
print(count)
