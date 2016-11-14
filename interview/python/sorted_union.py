def sorted_union(l1, l2):
    p1 = 0
    p2 = 0
    result = []
    while p1 < len(l1) and p2 < len(l2):
        to_add = 0
        if l1[p1] <= l2[p2]:
            to_add = l1[p1]
            p1 += 1
        else:
            to_add = l2[p2]
            p2 += 1
        if len(result) == 0 or (len(result) > 0 and to_add != result[len(result) - 1]):
            result.append(to_add)
    if p1 < len(l1):
        for i in range(p1, len(l1)):
            if len(result) > 0 and result[len(result) - 1] != l1[i]:
                result.append(l1[i])
    elif p2 < len(l2):
        for i in range(p2, len(l2)):
            if len(result) > 0 and result[len(result) - 1] != l2[i]:
                result.append(l2[i])
    print(result)


if __name__ == "__main__":
    l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    l2 = [1, 5, 10, 15, 20, 25]
    sorted_union(l1, l2)

    l1 = [1, 1, 1, 1, 1, 1]
    l2 = [1, 1, 1, 1, 1, 1]
    sorted_union(l1, l2)
