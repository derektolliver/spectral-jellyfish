def count():
    num_tests = int(input())
    for i in range(num_tests):
        num_list = [int(elem) for elem in input()]
        one_count = 0
        zero_count = 0
        num_matches = 0
        for j in range(0, len(num_list)):
            if num_list[j] == 1:
                one_count += 1
            else:
                num_matches += one_count
        print(num_matches)

if __name__ == "__main__":
    count()
