def eruption():
    num_tests = int(input())
    for i in range(num_tests):
        nums = [int(elem) for elem in input().split()]
        islands = nums[0]
        seconds = nums[1]
        island_eruptions = [int(elem) for elem in input().split()]
        num_surv = max(island_eruptions)
        print(num_surv + seconds)

if __name__ == "__main__":
    eruption()
