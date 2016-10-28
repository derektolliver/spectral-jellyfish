s = input()

alpha = set()
for elem in s:
    if elem != " " and elem.lower() not in alpha:
        alpha.add(elem.lower())
if len(alpha) == 26:
    print("pangram")
else:
    print("not pangram")
