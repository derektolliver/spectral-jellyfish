def wings():
    num_tests = int(input())
    for i in range(num_tests):
        info = [int(elem) for elem in input.split()]
        target = info[0]
        bull = info[1]
        wing_types = info[2]
        wing_list = []
        for j in range(wing_types):
            wing_list.append(int(input()))
        wing_list.sort()
        find_num_wings(target, bull, wing_list)

def find_num_wings(target, bull, wing_list):
    

if __name__ == "__main__":
    wings()
