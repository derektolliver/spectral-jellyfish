import sys

n,k = input().strip().split(' ')
n,k = [int(n),int(k)]
c = [int(c_temp) for c_temp in input().strip().split(' ')]

energy = 100
if n != k:
    index = k
    while index != 0:
        energy -= 1
        if c[index] == 1:
            energy -= 2
        index += k
        if index >= len(c):
            index -= len(c)
if c[0] == 1:
    energy -= 2
print(energy - 1)
