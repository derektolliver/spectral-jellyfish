# import sys, math
#
# n,m = input().strip().split(' ')
# n,m = [int(n),int(m)]
# c = [int(c_temp) for c_temp in input().strip().split(' ')]
#
# max_dist = 0
# for i in range(n):
#     min_dist = n - 1
#     for j in c:
#         if abs(i - j) < min_dist:
#             min_dist = abs(i - j)
#     if min_dist > max_dist:
#         max_dist = min_dist
# print(max_dist)

# import sys, math
#
# n,m = input().strip().split(' ')
# n,m = [int(n),int(m)]
# c_list = [int(c_temp) for c_temp in input().strip().split(' ')]
# c = set(c_list)
#
# max_dist = 0
# if len(c) == 1 and (0 in c or (n - 1) in c):
#     d1, d2 = abs(0 - c_list[0]), abs(n - c_list[0]) - 1
#     print(d1 if d1 > d2 else d2)
# else:
#     max_chain = 0
#     chain = 0
#     for i in range(n):
#         if i not in c:
#             chain += 1
#         else:
#             chain += 1
#             if max_chain < (chain // 2):
#                 max_chain = chain // 2
#             chain = 0
#     print(max_chain)
#
# import sys
#
# n,m = input().strip().split(' ')
# n,m = [int(n),int(m)]
# c_list = [int(c_temp) for c_temp in input().strip().split(' ')]
# c = set(c_list)
#
# max_chain = 0
# chain = 0
# for i in range(n):
#     if i not in c:
#         chain += 1
#     else:
#         chain += 1
#         if max_chain < (chain // 2):
#             max_chain = chain // 2
#         chain = 0
# lead_chain = c_list[0] - 0
# trail_chain = (n - 1) - c_list[len(c_list) - 1]
# print(max_chain if max_chain > lead_chain and max_chain > trail_chain else (lead_chain if lead_chain > trail_chain else trail_chain))

import sys

n,m = input().strip().split(' ')
n,m = [int(n),int(m)]
c_list = [int(c_temp) for c_temp in input().strip().split(' ')]
c_list.sort()
c = set(c_list)

chain_lengths = []
if c_list[0] >= 0:
    chain_lengths.append(c_list[0])
if ((n - 1) - c_list[len(c_list) - 1]) > 0:
    chain_lengths.append((n - 1) - c_list[len(c_list) - 1])
for i in range(m - 1):
    chain_lengths.append((c_list[i + 1] - c_list[i]) // 2)
print(max(chain_lengths))

# import sys, math
#
# n,m = input().strip().split(' ')
# n,m = [int(n),int(m)]
# c_list = [int(c_temp) for c_temp in input().strip().split(' ')]
# c_list.sort()
# c = set(c_list)
#
# max_dist = 0
# for s in range(n):
#     if s not in c:
#         lower = 0
#         upper = len(c_list)
#         while lower < upper:
#             # print(lower, upper, s)
#             mid = (lower + upper) // 2
#             if s < c_list[mid]:
#                 upper = mid - 1
#             else:
#                 lower = mid + 1
#         # lower == upper
#         if lower == c_list[0] and max_dist < abs(s - c_list[lower]):
#             print(s, abs(s - c_list[lower]), upper)
#             max_dist = abs(s - c_list[lower])
#         elif upper == c_list[len(c_list) - 1] and max_dist < abs(s - c_list[upper]):
#             print(s, abs(s - c_list[lower]), upper)
#             max_dist = abs(s - c_list[upper])
#         else:
#             if s < c_list[lower]:
#                 d1, d2 = abs(s - c_list[lower]), abs(s - c_list[lower - 1])
#                 d = d1 if d1 < d2 else d2
#                 if d > max_dist:
#                     max_dist = d
#             else:
#                 d1, d2 = abs(s - c_list[upper]), abs(s - c_list[upper + 1])
#                 d = d1 if d1 < d2 else d2
#                 if d > max_dist:
#                     max_dist = d
# print(max_dist)
