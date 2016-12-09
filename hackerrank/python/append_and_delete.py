import sys

# s = input().strip()
# t = input().strip()
# k = int(input().strip())
#
# def recurse(s_size, k, t_size):
#     if k == 0 and s_size == t_size:
#         return True
#     elif k > 0:
#         result = recurse(s_size + 1, k - 1, t_size)
#         if not result:
#             if s_size == 0:
#                 result = recurse(s_size, k - 1, t_size)
#             else:
#                 result = recurse(s_size - 1, k - 1, t_size)
#         return result
#
# print('Yes') if recurse(len(s), k, len(t)) else print('No')

s = input().strip()
t = input().strip()
k = int(input().strip())

if k >= (len(s) + len(t)):
    print('Yes')
else:
    num_shared = 0
    while len(s) > num_shared and len(t) > num_shared and s[num_shared] == t[num_shared]:
        num_shared += 1
    req_deletes = len(s) - num_shared
    req_adds = len(t) - num_shared
    k -= (req_deletes + req_adds)
    if k == 0 or (k > 0 and k % 2 == 0):
        print('Yes')
    else:
        print('No')
