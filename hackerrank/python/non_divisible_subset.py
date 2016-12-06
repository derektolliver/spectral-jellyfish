n, k = [int(elem) for elem in input().split()]

nums = [int(elem) for elem in input().split()]

keys = []
for i in range(k):
    keys.append(i)

remainder_map = {key: [] for key in keys}
for i in nums:
    remainder_map[i % k].append(i)

count = 0
visited = set()
for key in remainder_map:
    if key not in visited and len(remainder_map[key]) > 0:
        if key == 0 or k - key == key:
            count += 1
        elif len(remainder_map[key]) > len(remainder_map[k - key]):
                 count += len(remainder_map[key])
        elif len(remainder_map[k - key]) > len(remainder_map[key]):
                 count += len(remainder_map[k - key])
        visited.add(key)
        visited.add(k - key)
print(count)
