import sys

n,k,q = input().strip().split(' ')
n,k,q = [int(n),int(k),int(q)]
a = [int(a_temp) for a_temp in input().strip().split(' ')]

if k > len(a):
    k &= k & len(a)

b = [0] * len(a)
for i in range(len(a)):
    if i + k < len(a):
        b[i + k] = a[i]
    else:
        b[(i + k) - len(a)] = a[i]
a = b

for a0 in range(q):
    m = int(input().strip())
    print(a[m])
