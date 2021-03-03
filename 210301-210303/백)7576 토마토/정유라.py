# http://boj.kr/7576
from collections import deque
m, n = map(int, input().split())
tomato = []
q = deque()

for i in range(n):
    tomato.append(list(map(int, input().split())))
    for j in range(m):
        if tomato[i][j] == 1:
            q.append((i, j))

while q:
    x, y = q.popleft()

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if tomato[nx][ny] == 0:
                tomato[nx][ny] = tomato[x][y] + 1
                q.append((nx, ny))

# print(tomato)
MAX = -int(1e9)
isNotALL = False
for i in range(n):
    for j in range(m):
        if tomato[i][j] == 0:
            print(-1)
            isNotALL = True
            break
        if isNotALL:
            break
        MAX = max(MAX, tomato[i][j])

if not isNotALL:
    if MAX == 1:
        print(0)
    else:
        print(MAX-1)