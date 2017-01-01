from collections import deque

rooms, doors = [int(elem) for elem in input().split()]
graph = dict()
incoming = dict()
for i in range(doors):
    room, edge = [int(elem) for elem in input().split()]
    if room not in graph:
        graph[room] = []
    graph[room].append(edge)
    if room not in incoming:
        incoming[room] = 0
    if edge not in incoming:
        incoming[edge] = 1
    else:
        incoming[edge] += 1

zero_incoming = deque()
for k, v in incoming.items():
    if v == 0:
        zero_incoming.append(k)

topo = []
while len(zero_incoming) > 0:
    node = zero_incoming.popleft()
    topo.append(node)
    if node in graph:
        edges = graph[node]
        for e in edges:
            incoming[e] -= 1
            if incoming[e] == 0:
                zero_incoming.append(e)
                del incoming[e]
        del graph[node]

if len(graph) == 0:
    print("NO")
else:
    print("YES")
