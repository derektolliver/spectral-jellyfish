#Problem        : Zipline Hills
#Language       : Python 3
#Compiled Using : py_compile
#Version        : Python 3.4.3
#Input for your program will be provided from STDIN
#Print out all output from your program to STDOUT

# You operate a ziplining company and are setting up a new route on an ordered series of hills. (A 'zipline route' is a set of ziplines you can ride in order without hiking from hill to hill. For example, taking a zipline from hill A to B, and then taking another zipline from hill B to C, would be a route of length two.) As everyone knows, longer zipline routes are more fun! You want to know the length of the zipline route with the most individual ziplines possible.
#
# You know the height of each hill. Ziplines can only travel from one hill to another hill of lower height. Additionally, your ropes are only long enough to go at most two hills over. For example, from the fourth hill, you can set up a zipline going to the second, third, fifth, or sixth hills.
#
# Given a particular order of hill heights, print out the number of separate zipline connections in the longest route that meets the above constraints.

def find_path(index, path_len, hills):
    curr_len = path_len
    for i in range(index - 2, index + 3):
        if i >= 0 and i < len(hills) and hills[index] > hills[i]:
            curr_len = max(curr_len, find_path(i, path_len + 1, hills))
    return curr_len

num_hills = int(input())
hills = []
for h in range(0, num_hills):
    hills.append(int(input()))

longest = 0
for index in range(0, len(hills)):
    longest = max(longest, find_path(index, 0, hills))
print(longest)
