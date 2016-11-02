t = int(input())

for i in range(t):
    num_special = int(input())
    special_list = []
    for j in range(num_special):
        special_list.append(input())
    spec_set = set(special_list)
    num_flights = int(input())
    flights = []
    spec_flights = []
    for j in range(num_flights):
        f = input()
        if f not in spec_set:
            flights.append(f)
        else:
            spec_flights.append(f)
    flights.sort()
    spec_flights.sort()
    for j in spec_flights:
        print(j)
    for j in flights:
        print(j)
