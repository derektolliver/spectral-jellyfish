t = int(input())

for test in range(t):
    n, a, b = int(input()), int(input()), int(input())
    poss_end = set()
    for i in range(n):
        option = (n - i - 1) * a + i * b
        poss_end.add(option)
    results = list(poss_end)
    results.sort()
    for r in results:
        print(r, end=" ")
    print()
