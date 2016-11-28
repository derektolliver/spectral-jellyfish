import math

t = int(input())

for i in range(t):
    a, b = [int(elem) for elem in input().split()]
    print(math.floor(math.sqrt(b)) - math.ceil(math.sqrt(a) - 1))
