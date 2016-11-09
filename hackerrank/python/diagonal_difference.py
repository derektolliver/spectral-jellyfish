import sys
import math

n = int(input().strip())
a = []
for a_i in range(n):
    a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
    a.append(a_t)

d1 = 0
d2 = 0
for i in range(len(a)):
    d1 += a[i][i]
    d2 += a[i][len(a) - 1 - i]

print(abs(d1 - d2))
