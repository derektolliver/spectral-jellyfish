import sys

t = int(input().strip())
for a0 in range(t):
    n,c,m = input().strip().split(' ')
    n,c,m = [int(n),int(c),int(m)]
    result = n // c
    num_wrappers = result
    while num_wrappers >= m:
        temp = num_wrappers // m
        result += temp
        num_wrappers = temp + (num_wrappers % m)
    print(result)
