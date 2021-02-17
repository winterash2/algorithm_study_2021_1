# 문제
# 1. check배열 위치(bfs 안에 둬야함)
# 2. 종료 조건 (상어 찾는거 큐에서 꺼내자마자 ) 8방향 for문 안에 두니 시간초과가 나ㅣ지ㅣㅣㅣㅣㅣㅣㅣㅣ
from collections import deque

n, m = map(int, input().split())

# 아기 상어의 위치를 담은 그래프
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))


# 8가지 방향으로의 이동
dx = [0, 0, -1, 1, -1, -1, 1, 1]
dy = [-1, 1, 0, 0, -1, 1, -1, 1]


def bfs(d, x, y):
    # 방문처리를 위한 배열    
    check = [[0] * m for _ in range(n)]
    
    q = deque()
    q.append((d, x, y))
    check[x][y] = 1
    while q:
        d, x, y = q.popleft()
        if graph[x][y] == 1:
            return d
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
               
            if check[nx][ny] == 0:
                check[nx][ny] = 1
                q.append((d+1, nx, ny))


    return d

max_ = 0
for i in range(n):
    for j in range(m):
        max_ = max(max_, bfs(0, i, j))

print(max_)
