n = [int(elem) for elem in input().split(' ')]
costs = [int(elem) for elem in input().split(' ')]
charged = int(input())

k = n[1]
price = 0
for index in range(0, len(costs)):
    if index != k:
        price += costs[index]

price //= 2
if price == charged:
    print("Bon Appetit")
else:
    print(charged - price)
