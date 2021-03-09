import sys
input = sys.stdin.readline

n, m = map(int, input().split())
space = list(map(int, input().split()))
act = list(map(int, input().split()))

max_range = sum(act)
dp = [[0] * (max_range+1) for _ in range(n + 1)]
result = max_range

for i in range(1, n + 1):
    for j in range(1, max_range):
        if j < act[i - 1]:
            dp[i][j] = dp[i-1][j]
        elif j >= act[i-1]:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j - act[i - 1]] + space[i-1])
        if dp[i][j] >= m:
            result = min(result, j)

if m != 0:
    print(result)
else:
    print(0)

# https://claude-u.tistory.com/445
