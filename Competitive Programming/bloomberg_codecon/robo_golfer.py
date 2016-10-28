num_clubs = int(input())
clubs = [int(elem) for elem in input().split()]
num_holes = int(input())
holes = [int(elem) for elem in input().split()]
max_dist = max(clubs) + max(holes)

dp = [[False for _ in range(num_clubs + 1)] for _ in range(max_dist + 1)]

for i in range(len(dp[0])):
    dp[0][i] = True

for i in range(1, len(dp)):
    for j in range(1, len(dp[i])):
        # Check if previous club is within range and if combination of club reaches
        # or if the previous club could reach
        if i - clubs[j - 1] >= 0 and dp[i - clubs[j - 1]][j] or dp[i][j - 1]:
            dp[i][j] = True
for h in holes:
    reached = False
    for c in clubs:
        # If an overshot works, it is possible
        if dp[h + c][num_clubs]:
            reached = True
            print("yes")
            break
    if not reached:
        print("no")
