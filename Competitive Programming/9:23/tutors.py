for _ in range(int(input())):
    n, m = [int(i) for i in input().split()]
    scheduled = [0] * 100000
    for _ in range(n):
        i, j = [int(i) for i in input().split()]
        for index in range(i, j):
            scheduled[index] += 1
    for _ in range(m):
        print(scheduled[int(float(input()))])
