l = int(input())
h = int(input())

results = []
for i in range(l, h + 1):
    num = str(i ** 2)
    if len(num) < 2:
        l = 0
        r = int(num)
    else:
        l, r = int(num[:len(num) // 2]), int(num[len(num) // 2:])
    if l + r == i:
        results.append(i)

if len(results) == 0:
    print("INVALID RANGE")
else:
    for num in results:
        print(num, end=" ")
