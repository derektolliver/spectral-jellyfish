#!/bin/python3

import sys


s = input().strip()
n = int(input().strip())

letter_of_a = 0
for letter in s:
    if letter == 'a':
        letter_of_a += 1

a_count = letter_of_a * (n // len(s))

remainder = n % len(s)
for i in range(0, remainder):
    if s[i] == 'a':
        a_count += 1

print(a_count)
