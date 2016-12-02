i, j, k = [int(elem) for elem in input().split()]

def reverse(num):
    return int(str(num)[::-1])

count = 0
for n in range(i, j + 1):
    if (n - reverse(n)) % k == 0:
        count += 1

print(count)
