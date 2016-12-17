n, d = [int(elem) for elem in input().split()]

nums = [int(elem) for elem in input().split()]

visited = set(nums)
triplets = 0
for i in nums:
    if i - d in visited and i + d in visited:
        triplets += 1

print(triplets)
