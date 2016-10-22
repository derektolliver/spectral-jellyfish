#!/bin/python3

import sys


s = input().strip()

count = 1
for c in s:
    if c != c.lower():
        count += 1
print(count)
