import sys
import math

n,m = input().strip().split(' ')
n,m = [int(n),int(m)]
a = [int(a_temp) for a_temp in input().strip().split(' ')]
a.sort()
b = [int(b_temp) for b_temp in input().strip().split(' ')]
b.sort()

factors = [set() for i in range(m)]
for i in range(len(b)):
    for j in range(1, math.floor(math.sqrt(b[i])) + 1):
        if b[i] % j == 0:
            factors[i].add(j)
            factors[i].add(b[i] // j)

result = [x for x in set.intersection(*factors)]
result.sort()
for i in a:
    list_copy = [x for x in result]
    for j in result:
        if j % i != 0:
            list_copy.remove(j)
    result = [x for x in list_copy]

print(len(result))
