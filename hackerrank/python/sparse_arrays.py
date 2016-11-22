num_strings = int(input())
string_dict = dict()
for i in range(num_strings):
    s = input()
    if s in string_dict:
        string_dict[s] += 1
    else:
        string_dict[s] = 1

num_queries = int(input())
for i in range(num_queries):
    s = input()
    if s in string_dict:
        print(string_dict[s])
    else:
        print(str(0))
