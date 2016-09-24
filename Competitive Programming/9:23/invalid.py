def invalid():
    num_tests = int(input())
    for i in range(num_tests):
        invalid_num = 0
        num_friends = int(input())
        for f in range(num_friends):
            info = [int(elem) for elem in input().split()]
            if info[0] < 6 or info[0] > 21 or info[1] < 0 or info[1] > 1024:
                invalid_num = invalid_num + 1
        print(invalid_num)

if __name__ == "__main__":
    invalid()
