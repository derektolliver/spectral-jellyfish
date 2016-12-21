import sys

def check_neighbors(grid, i, j):
    if i - 1 >= 0 and i + 1 < len(grid) and j - 1 >= 0 and j + 1 < len(grid[i]):
        return grid[i - 1][j] < grid[i][j] and grid[i + 1][j] < grid[i][j] and grid[i][j - 1] < grid[i][j] and grid[i][j + 1] < grid[i][j]
    return False

def grid_maker(grid):
    new_grid = []
    for i in range(len(grid)):
        row = []
        for j in range(len(grid[i])):
            if check_neighbors(grid, i, j):
                row.append('X')
            else:
                row.append(str(grid[i][j]))
        new_grid.append(row)
    return new_grid

n = int(input().strip())
grid = []
for grid_i in range(n):
   grid_t = list(input().strip())
   grid.append(grid_t)

grid = grid_maker(grid)
for i in grid:
    for j in i:
        print(j, end="")
    print()
