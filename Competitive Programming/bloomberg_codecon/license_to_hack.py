#Problem        : License to Hack
#Language       : Python 3
#Compiled Using : py_compile
#Version        : Python 3.4.3
#Input for your program will be provided from STDIN
#Print out all output from your program to STDOUT

# MI6 and CIA have been trying to intercept terrorist communications, but found that all their messages are transmitted in a very cryptic way. 007 was called to the rescue to crack the code. 007 has figured out the algorithm the terrorists have used to encode the message, but needs our help to code in the reverse and find the actual message from the encryption.
# 
# The encoding Algorithm figured out by 007 is as follows:
#
# Given a message of any length and a positive integer N, reverse N characters and skip N characters until the end of the string to generate the encrypted message.

import sys

def reverse_string(word, num):
    result = ""
    count = 0
    for index in range(0, len(word), num):
        if count % 2 == 0:
            temp = ""
            if index + num >= len(word):
                temp = word[index : len(word)]
            else:
                temp = word[index : index + num]
            result += temp[::-1]
        else:
            result += word[index : index + num]
        count += 1
    return result

word = input()
num = int(input())

print(reverse_string(word, num))

# data = sys.stdin.read().splitlines()
#
# word = ""
# num = 0
# for index in range(0, len(data)):
#     if index % 2 == 0:
#         word = str(data[index])
#     else:
#         num = int(data[index])
#         print(reverse_string(word, num))
