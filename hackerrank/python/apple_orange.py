import sys

s,t = input().strip().split(' ')
s,t = [int(s),int(t)]
a,b = input().strip().split(' ')
a,b = [int(a),int(b)]
m,n = input().strip().split(' ')
m,n = [int(m),int(n)]
apple = [int(apple_temp) for apple_temp in input().strip().split(' ')]
orange = [int(orange_temp) for orange_temp in input().strip().split(' ')]

apple_hits, orange_hits = 0, 0
for i in apple:
    if a + i >= s and a + i <= t:
        apple_hits += 1

for i in orange:
    if b + i >= s and b + i <= t:
        orange_hits += 1

print(apple_hits)
print(orange_hits)
