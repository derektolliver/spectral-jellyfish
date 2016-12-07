from collections import defaultdict

n = int(input())
nums = [int(elem) for elem in input().split()]

num_map = defaultdict(int)
for i in nums:
    num_map[i] += 1

if len(num_map.items()) > 0:
	most_frequent_key = 0
	greatest_number_of_elems = 0
	for key in num_map:
		if num_map[key] > greatest_number_of_elems:
			most_frequent_key = key
			greatest_number_of_elems = num_map[key]

	count = 0
	for i in nums:
	    if i != most_frequent_key:
	        count += 1
	print(count)
else:
	print(0)
