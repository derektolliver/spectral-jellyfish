num_chems = int(input())
chems = dict()
for c in range(0, num_chems):
    info = [elem for elem in input().split(' ')]
    name = info[0]
    elems = set()
    for e in range(2, len(info)):
        elems.add(info[e])
    chems[name] = elems

recipe = [elem for elem in input().split(' ')]
visited = set()
safe = True
for c in recipe:
    if c in chems:
        for elem in chems[c]:
            if elem not in visited:
                safe = False
                break
    if not safe:
        break
    visited.add(c)
if safe:
    print("SAFE!")
else:
    print("BOOM!")
