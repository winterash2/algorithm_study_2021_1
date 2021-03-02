import sys
input = sys.stdin.readline

mx = [0,0,1,-1]
my = [1,-1,0,0]

def dfs(x, y):
    field[x][y] = 0
    visit[x][y] = 0
    for i in range(4):
        nx = x + mx[i]
        ny = y + my[i]
        if 0 <= nx < n and 0 <= ny < m and visit[nx][ny]:
            if field[nx][ny] == 1:
                dfs(nx, ny)
            else:
                continue

T = int(input())
for _ in range(T):
    m, n, k = map(int, input().split())
    field = [[0] * m for _ in range(n)]
    visit = [[1] * m for _ in range(n)]
    for _ in range(k):
        y, x = map(int, input().split())
        field[x][y] = 1
    
    cnt = 0
    for i in range(n):
        for j in range(m):
            visit[i][j] = 0
            if field[i][j] == 1:
                dfs(i,j)
                cnt += 1
    
    print(cnt)
