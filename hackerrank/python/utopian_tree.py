import sys

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    h = 1
    for i in range(n):
        if (i + 1) % 2 == 0:
            h += 1
        else:
            h *= 2
    print(h)
