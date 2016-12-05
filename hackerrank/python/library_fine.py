import sys

d1,m1,y1 = input().strip().split(' ')
d1,m1,y1 = [int(d1),int(m1),int(y1)]
d2,m2,y2 = input().strip().split(' ')
d2,m2,y2 = [int(d2),int(m2),int(y2)]

result = 0
if y1 > y2:
    result = 10000
elif m1 > m2 and y1 == y2:
    result = 500 * (m1 - m2)
elif d1 > d2 and m1 == m2 and y1 == y2:
    result = 15 * (d1 - d2)
print(result)
