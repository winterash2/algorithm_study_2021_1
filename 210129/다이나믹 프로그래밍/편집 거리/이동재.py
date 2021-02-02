base = list(input())
goal = list(input())

INF = float("INF")

# base = list("sunday")
# goal = list("saturday")
# base = list("cut")
# goal = list("cat")


dp = [[INF for _ in range(len(goal))] for _ in range(len(base))]
for j in range(len(goal)):
    dp[0][j] = j
for i in range(len(base)):
    dp[i][0] = i

for i in range(1, len(base)):
    for j in range(1, len(goal)):
        if base[i] == goal[j]:
            dp[i][j] = dp[i-1][j-1]
        else:
            dp[i][j] = 1 + min(
                    dp[i-1][j-1],
                    dp[i-1][j],
                    dp[i][j-1]
                )

print(dp[len(base)-1][len(goal)-1])