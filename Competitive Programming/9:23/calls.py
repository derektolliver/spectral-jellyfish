import math


for _ in range(int(input())):
    n = []
    m = []
    for i in range(int(input())):
        ni, mi = [int(i) for i in input().split()]
        n.append(ni)
        m.append(mi)
    calls = [(n[i] * m[i], i) for i in range(len(n))]
    maximum = max(calls)[0]
    count = 0
    for i in range(len(n)):
        count += maximum // n[i]
    print(count)
