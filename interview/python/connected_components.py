def find_connection(grid):
    great = 0
    visited = set()
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if grid[r][c] == 1:
                temp = dfs(grid, visited, r, c)
                if temp > great:
                    great = temp
    return great

def dfs(grid, visited, r, c):
    if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[r]) or grid[r][c] == 0 or (r, c) in visited:
        return 0
    else:
        visited.add((r, c))
        temp = 1
        temp += dfs(grid, visited, r - 1, c)
        temp += dfs(grid, visited, r + 1, c)
        temp += dfs(grid, visited, r, c - 1)
        temp += dfs(grid, visited, r, c + 1)
        return temp


if __name__ == "__main__":
    test = [[1, 0, 0, 0, 1],
            [1, 1, 1, 1, 0],
            [0, 0, 0, 1, 0]]
    print(find_connection(test))

    test = [[0, 0, 0, 1, 0],
            [1, 0, 1, 1, 1],
            [1, 1, 1, 0, 0],
            [0, 0, 0, 1, 1],
            [0, 0, 0, 1, 1]]
    print(find_connection(test))
