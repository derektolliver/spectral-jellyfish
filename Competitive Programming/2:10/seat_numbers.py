t = int(input())

for i in range(t):
    seat = input()
    num_rows = seat[len(seat) - 1]
    seat = seat[0:len(seat) - 1]
    print(int(seat) * 6)
