n = int(input())
nums = [int(elem) for elem in input().split()]
ind_to_val = dict()

count = 1
for i in nums:
    ind_to_val[i] = count
    count += 1

for i in range(1, len(nums) + 1):
    print(ind_to_val[ind_to_val[i]])
