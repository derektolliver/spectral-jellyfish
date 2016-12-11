import sys

t = int(input().strip())
for a0 in range(t):
    b,w = input().strip().split(' ')
    b,w = [int(b),int(w)]
    x,y,z = input().strip().split(' ')
    x,y,z = [int(x),int(y),int(z)]
    smaller, greater, small_count, great_count = 0, 0, 0, 0
    if x < y:
        smaller = x
        small_count = b
        greater = y
        great_count = w
    else:
        smaller = y
        small_count = w
        greater = x
        great_count = b
    if smaller + z < greater:
        greater = smaller + z
    print(smaller * small_count + greater * great_count)
