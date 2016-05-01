def zombie():
    num_tests = int(input())
    for i in range(num_tests):
        info = [int(elem) for elem in input().split()]
        rows = info[0]
        cols = info[1]
        ops = info[2]
        matrix = []
        for j in range(rows):
            row = [int(elem) for elem in input()]
            matrix.append(row)
        for j in range(ops):
            op = input().split()
            command = op[0]
            mod_num = int(op[1])
            if command == 'R':
                for r in range(rows):
                    if r % mod_num == 0:
                        for c in range(cols):
                            if matrix[r][c] == 1:
                                matrix[r][c] = 0
                            else:
                                matrix[r][c] = 1
            else:
                for c in range(cols):
                    if c % mod_num == 0:
                        for r in range(rows):
                            if matrix[r][c] == 1:
                                matrix[r][c] = 0
                            else:
                                matrix[r][c] = 1
        for r in range(rows):
            for c in range(cols):
                val = matrix[r][c]
                print(val, end="")
            print()

if __name__ == "__main__":
    zombie()
