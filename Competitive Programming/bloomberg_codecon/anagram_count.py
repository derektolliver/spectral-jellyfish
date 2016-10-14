#Problem        : Anagram Count
#Language       : Python 3
#Compiled Using : py_compile
#Version        : Python 3.4.3
#Input for your program will be provided from STDIN
#Print out all output from your program to STDOUT

num_words = int(input())
words = []
for i in range(0, num_words):
    temp = input().lower()
    words.append(''.join(sorted(temp)))

anagrams = dict()
for s in words:
    if s in anagrams:
        anagrams[s] += 1
    else:
        anagrams[s] = 1

count = 0
for key in anagrams:
    if anagrams[key] >= 2:
        count += anagrams[key]

print(count)
