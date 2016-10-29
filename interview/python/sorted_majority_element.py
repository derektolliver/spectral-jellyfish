# Majority Element
# [3,5,4,3,1,3,3,3] -> 3
# [1,7,8] -> ??
# [1,2,3,2] -> ??

from collections import defaultdict

def maj_ele(nums):
    num_to_freq = defaultdict()
    for n in nums:
        num_to_freq[n] += 1
    for k in num_to_freq:
        if num_to_freq[k] > len(nums) // 2:
            return k
    raise InputException


# [5,6,7,7,7] -> 7
# def get_count(nums, n):
#     count = 0
#     curr_index = len(nums) // 2
#     left_bound = 0
#     right_bound = len(nums) - 1
#     if nums[curr_index] == n:
#         while nums[curr_index + right_bound // 2] != n or ((right_bound + curr_index // 2) < len(nums) or nums[(right_bound + curr_index // 2) + 1] > n:
#             right_bound = right_bound + curr_index // 2
#         while nums[curr_index + left_bound // 2] != n or
#
#
#             if nums[right_bound] > n:
#                 right_bound -= (right_bound - curr_index) // 2
#             if
#         if nums[right_bound] == n:
#             count = right_bound - curr_index
#         else:
#             right_bound

def maj_ele_sorted(nums):
    left_bound = 0
    second_index = (len(nums) // 2) + 1
    curr_index = 0
    if nums[left_bound] != nums[second_index]:
        elem = nums[second_index]
        while nums[curr_index] != elem and (curr_index > 0 and nums[curr_index - 1] == elem):
            if nums[curr_index] == elem:
                second_index = curr_index
            else:
                left_bound = curr_index
            curr_index = left_bound + second_index // 2
    if nums[curr_index] == nums[curr_index + (len(nums) // 2) + 1]:
        return nums[curr_index]
    raise InputException
