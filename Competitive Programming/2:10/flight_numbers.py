t = int(input())

for i in range(t):
    num_flights = int(input())
    flights = [int(elem) for elem in input().split()]
    sol = 0
    for j in flights:
        bi_rep = "{0:b}".format(j)
        xor = int(bi_rep[0])
        for c in range(1, len(bi_rep)):
            xor ^= int(bi_rep[c])
        if xor == 1:
            sol += 1
    print(sol)
