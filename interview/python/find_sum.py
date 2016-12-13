nums = [int(elem) for elem in input().split()]
tgt_sum = int(input())

front = 0
back = len(nums) - 1
curr_sum = nums[front] + nums[back]
while front < back and curr_sum != tgt_sum:
    curr_sum = nums[front] + nums[back]
    if curr_sum < tgt_sum:
        front += 1
    elif curr_sum > tgt_sum:
        back -= 1

if curr_sum == tgt_sum:
    print('Yes')
else:
    print('No')
