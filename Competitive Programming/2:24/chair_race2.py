from collections import deque

rooms, doors = [int(elem) for elem in input().split()]
graph = dict()
for i in range(doors):
    room, edge = [int(elem) for elem in input().split()]
    if room not in graph:
        graph[room] = set()
    graph[room].add(edge)

for k, v in graph.items():
    stack = deque()
    visited = set()
    stack.append(k)
    possible = False
    while stack:
        n = stack.pop()
        if n not in visited:
            temp.add(n)
            visited.add(n)
            if n in graph:
                stack.extend(graph[n] - visited)
        else:
            possible = True
            break
    if possible:
        print("YES")
        break
else:
    print("NO")
