import sys

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    nums = [int(elem) for elem in str(n)]
    count = 0
    for i in nums:
        if i != 0 and n % i == 0:
            count += 1
    print(count)
