"""
Given a range of integers (a,b) and an integer K, implement add for a list such that you are only adding integers in the range (a,b)
AND you can't add an integer if there exists another integer in the list that is within K units of that element.

This means if we k = 3 and we do add(2), we can't add -1, 0, 1, 2, 3, 4, or 5 because 2-3 = -1 and 2 + 3 = 5

Do this in O(1)
"""

# O(k) solution
# def range_add(k, nums, ran):
#     result = []
#     cant_add = set()
#     for i in nums:
#         if i not in cant_add:
#             result.append(i)
#             cannot_add_more(cant_add, i)
#     return result
#
# def cannot_add_more(cant_add, num):
#     for i in range(num - 3, num + 4):
#         if i != num:
#             cant_add.add(i)

# O(1) solution
def range_add(k, ran, nums):
    min_num = ran[0] - 1
    buckets = [min_num] * ((abs(ran[1] - ran[0]) + 1) // k)
    if len(buckets) % k != 0:
        buckets.append(min_num)
    result = []
    for i in range(len(nums)):
        bucket_index = (abs(nums[i] - ran[0]) + 1) // k
        poss_num = nums[i]
        if buckets[bucket_index] == min_num and (bucket_index - 1 < 0 or (buckets[bucket_index - 1] == min_num or buckets[bucket_index - 1] < poss_num - k)) and (bucket_index + 1 >= len(buckets) or (buckets[bucket_index + 1] == min_num or buckets[bucket_index + 1] > poss_num + k)):
            result.append(poss_num)
            buckets[bucket_index] = poss_num
    return result


if __name__ == "__main__":
    k = 3
    ran = (-2, 11)
    test = [2, 3, 7, 9, 11, -1, -2]
    print(range_add(k, ran, test))

    k = 100
    ran = (0, 100)
    test = [16, 18, 100, 69, 48, 42, 70, 26]
    print(range_add(k, ran, test))

# N / K
