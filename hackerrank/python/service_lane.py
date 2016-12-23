import sys

n,t = input().strip().split(' ')
n,t = [int(n),int(t)]
width = [int(width_temp) for width_temp in input().strip().split(' ')]
for a0 in range(t):
    i,j = input().strip().split(' ')
    i,j = [int(i),int(j)]
    smallest = 3
    for index in range(i, j + 1):
        if width[index] < smallest:
            smallest = width[index]
    print(smallest)
