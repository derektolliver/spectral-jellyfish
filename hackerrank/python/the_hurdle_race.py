import sys

n,k = input().strip().split(' ')
n,k = [int(n),int(k)]
height = list(map(int, input().strip().split(' ')))
print(max(height) - k) if (max(height) - k) > 0 else print(0)
