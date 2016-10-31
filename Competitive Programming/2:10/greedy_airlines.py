t = int(input())

for i in range(t):
    num_pass, req_num = [int(elem) for elem in input().split()]
    asking = [int(elem) for elem in input().split()]
    asking.sort()
    sol = 0
    for j in range(num_pass - req_num):
        sol += asking[j]
    print(sol)
