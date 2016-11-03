t = int(input())

for i in range(t):
    num_speeds = int(input())
    avg = 0
    total_sec = 0
    for j in range(num_speeds):
        speed, sec = [int(elem) for elem in input().split()]
        total_sec += sec
        avg += (speed * sec)
    print(round(avg / total_sec))
