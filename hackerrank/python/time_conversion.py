import sys

CLOCK_CONST = 12

time = input().strip()

if time[-2] == 'A' and time[:2] == '12':
    time = '00' + time[2:]
elif time[-2] == 'P' and time[:2] != '12':
    time = str(int(time[:2]) + CLOCK_CONST) + time[2:]
print(time[:-2])
