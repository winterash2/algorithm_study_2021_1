from collections import deque
import sys
input = sys.stdin.readline

mx = [0, 0, 1, -1]
my = [1, -1, 0, 0]

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]


def dfs(x, y):
    if x == (n-1) and y == (m-1):
        return 1
    if dp[x][y] == -1:
        dp[x][y] = 0

        now = arr[x][y]
        for i in range(4):
            dx = x + mx[i]
            dy = y + my[i]
            if 0 <= dx < n and 0 <= dy < m:
                if now > arr[dx][dy]:
                    dp[x][y] += dfs(dx, dy)
    return dp[x][y]


dp = [[-1] * m for _ in range(n)]

print(dfs(0, 0))
print(dp)
