def answer(maze):
    offsets = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    return dfs(maze, len(maze[0]), len(maze), (0, 0), offsets, dict(), False)

def check_bounds(point, width, height):
    if point[0] < 0 or point[0] >= height or point[1] < 0 or point[1] >= width:
        return True
    return False

def dfs(maze, w, h, point, offsets, path_mins, unblock):
    if point[0] == h - 1 and point[1] == w - 1:
        return 1

    if (point, unblock) in path_mins:
        return path_mins[(point, unblock)]

    result = w * h
    path_mins[(point, unblock)] = result

    for of in offsets:
        next_point = (point[0] + of[0], point[1] + of[1])
        if not check_bounds(next_point, w, h):
            if maze[next_point[0]][next_point[1]] == 0:
                result = min(dfs(maze, w, h, next_point, offsets, path_mins, unblock), result)
            elif maze[next_point[0]][next_point[1]] == 1 and not unblock:
                result = min(dfs(maze, w, h, next_point, offsets, path_mins, True), result)

    result += 1
    path_mins[(point, unblock)] = result
    return result

if __name__ == "__main__":
    maze = [[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]]
    print(answer(maze))
