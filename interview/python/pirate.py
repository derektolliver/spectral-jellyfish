[1, 4, 6, 7, 8, 8, 9, 11, 14, 16, 20]
[2, 3, 4, 5, 8, 10, 11, 11, 21]
{4, 8, 8, 11, 11}

[1,1,1,1]
[1,1,1,1,1,1,1,1]


def inter(l1, l2):
    hold = set()
    shared = []
    for i in l1:
        if i not in hold:
            hold.add(i)
    for i in l2:
        if i in hold:
            shared.add(i)
    return shared

[10, 10, 15, 15, 30, 40], 25
true

def pirate(treasure, request):
    treasure.sort()
    for i in range(0, len(treasure)):
        if (recurse(treasure, i, treasure[i], request))
            return true
    return false

def recurse(treasure, index, curr_val, request):
    if curr_val == request:
        return true
    while index < len(treasure):
        index += 1
        if recurse(treasure, index, curr_val + treasure[index], request)
            return true
    return false


[1, 2, 4]

1
1, 2
1, 2, 4
1, 4
2,
2, 4
4
[]
