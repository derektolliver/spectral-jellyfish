def answer(l):
    count = 0
    for i in range(1, len(l) - 1):
        left = []
        right = []
        for j in range(0, i):
            if l[i] % l[j] == 0:
                left.append(l[j])
        for j in range(i + 1, len(l)):
            if l[j] % l[i] == 0:
                right.append(l[j])
        count += len(left) * len(right)

    return count


if __name__ == "__main__":
    test = [5, 5, 5, 5, 5]
    print(answer(test))
