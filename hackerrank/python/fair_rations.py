import sys

N = int(input().strip())
B = [int(B_temp) for B_temp in input().strip().split(' ')]

if sum(B) % 2 == 0:
    count = 0
    for i in range(len(B)):
        if B[i] % 2 != 0:
            j = i
            while j < len(B) - 1 and B[j] % 2 != 0:
                B[j] += 1
                B[j + 1] += 1
                count += 2
                j += 1
            i = j
    print(count)
else:
    print("NO")
