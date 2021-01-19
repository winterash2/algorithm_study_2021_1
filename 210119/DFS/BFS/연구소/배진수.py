def count_zero():
    count = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                count += 1
    return count

def virus(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if temp[nx][ny] == 0:
                temp[nx][ny] = 2
                virus(nx, ny)

def dfs(wall):
    global result
    if wall == 3:
        for i in range(n):
            for j in range(m):
                temp[i][j] = lab[i][j]
        
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    virus(i, j)     
        result = max(result, count_zero())
        return

    for i in range(n):
        for j in range(m):
            if lab[i][j] == 0:
                lab[i][j] = 1
                wall += 1
                dfs(wall)
                lab[i][j] = 0
                wall -= 1

n, m = map(int, input().split())
lab = []
temp = [[0] * m for _ in range(n)]

for _ in range(n):
    lab.append(list(map(int, input().split())))

# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

result = 0
dfs(0)
print(result)