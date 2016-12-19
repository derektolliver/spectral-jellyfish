import sys

n = int(input().strip())
A = [int(A_temp) for A_temp in input().strip().split(' ')]

num_to_index = dict()
distances = dict()
for index in range(len(A)):
    if A[index] not in num_to_index:
        num_to_index[A[index]] = index
    else:
        distances[A[index]] = index - num_to_index[A[index]]

minimum_distance = len(A)
for d in distances:
    if minimum_distance > distances[d]:
        minimum_distance = distances[d]

if minimum_distance == len(A):
    print(-1)
else:
    print(minimum_distance)
