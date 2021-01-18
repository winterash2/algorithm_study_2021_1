n, m = map(int, input().split())
icebox = [] * n
icebox = [list(map(int, input())) for _ in range(n)]


def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    if icebox[x][y] == 0:
        icebox[x][y] = 1
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y + 1)
        dfs(x, y - 1)
        return True
    return False


count = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j):
            count += 1
print(count)
