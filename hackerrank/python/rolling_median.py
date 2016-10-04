import heapq

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))

min_h = []
max_h = []

for elem in a:
    equal = False
    if len(max_h) != len(min_h):
        heapq.heappush(min_h, heapq.heappop(max_h)[1])
        equal = True
    heapq.heappush(max_h, (-elem, elem))
    if equal:
        print((max_h[0][1] + min_h[0]) / 2)
    else:
        print(max_h[0][1] / 1.0)
    a.append(int(input()))
