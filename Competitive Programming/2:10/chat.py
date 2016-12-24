from collections import deque

t = int(input())

for i in range(t):
    num_actions = int(input())
    names = deque()
    deleted = set()
    for j in range(num_actions):
        li = [elem for elem in input().split()]
        if li[0] == "DELETE":
            if len(names) > 0:
                name = names.popleft()
                while name in deleted and len(names) > 0:
                    name = names.popleft()
                if name not in deleted:
                    print(name)
                    deleted.add(name)
                if name in deleted and len(names) == 0:
                    print("NONE")
            else:
                print("NONE")
        else:
            name = li[1]
            if name in deleted:
                deleted.remove(name)
            names.appendleft(name)
    print()
