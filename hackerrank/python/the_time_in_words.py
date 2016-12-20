import sys

num_minutes = 60
words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'quarter', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty', 'twenty one', 'twenty two', 'twenty three', 'twenty four', 'twenty five', 'twenty six', 'twenty seven', 'twenty eight', 'twenty nine']

h = int(input().strip())
m = int(input().strip())

result = ""
if m == 0:
    result = words[h - 1] + " o' clock"
elif m < 30:
    result += words[m - 1]
    if m == 1:
        result += " minute"
    elif m != 15:
        result += " minutes"
    result += " past " + words[h - 1]
elif m == 30:
    result = "half past " + words[h - 1]
else:
    h += 1
    result += words[num_minutes - m - 1]
    if num_minutes - m == 1:
        result += " minute"
    elif num_minutes - m != 15:
        result += " minutes"
    result += " to " + words[h - 1]

print(result)
