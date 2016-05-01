def chase():
    num_tests = int(input())
    for i in range(num_tests):
        num_doors = int(input())
        graph = {}
        for j in range(num_doors):
            node = [int(elem) for elem in input().split()]
            if node[0] in graph:
                graph[node[0]].add(node[1])
            else:
                set_nodes = set()
                set_nodes.add(node[1])
                graph[node[0]] = set_nodes
        visited = set()
        visited.add(1)
        done = False
        for k in graph:
            for l in graph[k]:
                if l in visited:
                    print("SURVIVE")
                    done = True
                    break
                else:
                    visited.add(l)
            if done:
                break
        if not done:
            print("DEAD")

if __name__ == "__main__":
    chase()
