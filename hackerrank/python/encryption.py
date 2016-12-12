import sys
import math

s = input().strip()
num_rows = math.floor(math.sqrt(len(s)))
num_cols = math.ceil(math.sqrt(len(s)))
if len(s) > num_rows * num_cols:
    num_rows += 1

matrix = [[0 for c in range(num_cols)] for r in range(num_rows)]
for r in range(num_rows):
    for c in range(num_cols):
        index = r * len(matrix[0]) + c
        if index < len(s):
            matrix[r][c] = s[index]

result = ""
for c in range(num_cols):
    for r in range(num_rows):
        if matrix[r][c] != 0:
            result += matrix[r][c]
    if c != num_cols - 1:
        result += ' '

print(result)
