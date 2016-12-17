nums = [int(elem) for elem in input().split()]
tgt_sum = int(input())

# Sorted solution
# front, back = 0, len(nums) - 1
# curr_sum = nums[front] + nums[back]
# while front < back and curr_sum != tgt_sum:
#     curr_sum = nums[front] + nums[back]
#     if curr_sum < tgt_sum:
#         front += 1
#     elif curr_sum > tgt_sum:
#         back -= 1
#
# if curr_sum == tgt_sum:
#     print('Yes')
# else:
#     print('No')

# Non-sorted solution
visited = set()
found = False
for i in nums:
    if tgt_sum - i in visited:
        print('Yes')
        found = True
        break
    visited.add(i)
if not found:
    print('No')
