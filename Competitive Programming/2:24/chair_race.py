from collections import defaultdict

def recurse(graph, visited, curr_room):
    if curr_room in visited:
        return True
    visited.add(curr_room)
    if curr_room in graph:
        for edge in graph[curr_room]:
            if recurse(graph, visited, edge):
                return True
    visited.remove(curr_room)
    return False

def race():
    rooms, doors = [int(elem) for elem in input().split()]
    graph = dict()
    for i in range(doors):
        room, edge = [int(elem) for elem in input().split()]
        if room not in graph:
            graph[room] = []
        graph[room].append(edge)

    visited = set()
    possible = False
    for k, v in graph.items():
        possible = recurse(graph, visited, k)
        if possible:
            print("YES")
            break
    else:
        print("NO")

if __name__ == "__main__":
    race()
