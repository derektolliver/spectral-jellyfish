n = int(input())
elements = [int(elem) for elem in input().split()]

if elements == sorted(elements):
    print("yes")
else:
    asc_elems = list(elements)
    asc_elems.sort()
    indices = []
    for i in range(len(elements)):
        if elements[i] != asc_elems[i]:
            indices.append(i)
    if len(indices) == 2:
        print("yes")
        print("swap", indices[0] + 1, indices[1] + 1)
    elif len(indices) > 2:
        first = elements[0:indices[0]]
        middle = elements[indices[0]:(indices[len(indices) - 1] + 1)]
        middle = middle[::-1]
        last = elements[indices[len(indices) - 1] + 1:len(elements)]
        elements = first + middle + last
        if elements == asc_elems:
            print("yes")
            print("reverse", indices[0] + 1, indices[len(indices) - 1] + 1)
        else:
            print("no")
    else:
        print("no")
