def new_year():
    num_tests = int(input())
    for i in range(numTests):
        info = [int(elem) for elem in input().split()]
        num_ports = info[0]
        flights = info[1]
        port_map = dict()
        for j in range(flights):
            ride = [int(elem) for elem in input().split()]
            first = ride[0]
            second = ride[1]
            if first not in port_map:
                arrivals = []
                arrivals.append(second)
                port_map[first] = arrivals
            else:
                arrivals = port_map[first]
                arrivals.append(second)
    check_dict(port_map)

def check_dict(port_map):
    max_num_flights = 0
    for depart in port_map.keys():
        arrivals = port_map[depart]
        flight_list = []
        for arrival in arrivals:
            flight_list = find_max_flights(port_map, arrival, flight_list[])
        if size(flight_list) > max_num_flights:
            max_num_flights = size(flight_list)

def find_max_flights(port_map, depart, flight_list):
    if depart in flight_list:
        return flight
    for arrival in port_map[depart]:
        find_max_flights(port_map, arrival)



if __name__ == "__main__":
    new_year()
