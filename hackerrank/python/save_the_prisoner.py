tests = int(input())

for t in range(tests):
    n, m, s = [int(elem) for elem in input().split()]
    m -= 1
    if m >= n:
        m %= n
    result = 0
    if (s + m) > n:
        result = (s + m) - n
    else:
        result = s + m
    print(result)
