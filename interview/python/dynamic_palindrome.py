# Complete the function below.

BASE_NUMS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'e', 'f', 'g', 'h', 'i', 'j']
BINARY = 2

def find_number(k, n):
    count = 0
    val = find_start(k)
    while count < n:
        val = find_val(val + 1, k)
        count += 1
    return val

def find_start(k):
    result = 0
    for i in range(k):
        result += 2 ** i
    return result - 1

def find_val(val, k):
    while not is_palindrome(to_base_k(k, val)) or not contains_consecutive_ones(k, to_base_k(BINARY, val)):
        val += 1
    return val

def to_base_k(k, val):
    result = ""
    while val != 0:
        result = str(BASE_NUMS[val % k]) + result
        val //= k
    return result

def is_palindrome(base_k_num):
    length = len(base_k_num)
    for index in range(length // 2):
        if base_k_num[index] != base_k_num[length - 1 - index]:
            return False
    return True

def contains_consecutive_ones(k, base_two_num):
    index = 0
    count = 0
    while index < len(base_two_num) and count < k:
        if base_two_num[index] == '1':
            count += 1
        else:
            count = 0
        index += 1
    if count >= k:
        return True
    return False
