import sys
input = sys.stdin.readline

n, k = map(int, input().split())

obj = [0] * n
for i in range(n):
    a, b = map(int, input().split())
    obj[i] = (a, b)

obj.sort()
dp = [[0] * (k+1) for _ in range(n + 1)]

for i in range(1, n+1):
    for j in range(1, k+1):
        wei, val = obj[i-1]
        if wei > j:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], val + dp[i-1][j - obj[i-1][0]])

print(dp[-1][-1])
# print(dp)
