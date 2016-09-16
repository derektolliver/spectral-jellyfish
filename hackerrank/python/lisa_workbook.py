n, k = [int(elem) for elem in input().split()]
chapter_counts = [int(elem) for elem in input().split()]

page = 1
special_pages = 0
for ch in chapter_counts:
    problem = 1
    for i in range(ch):
        if problem == page:
            special_pages += 1
        if problem < ch and problem % k == 0:
            page += 1
        problem += 1
    page += 1

print(special_pages)
