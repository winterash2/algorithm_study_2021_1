# 백준 2178
from collections import deque

n, m = map(int, input().split())
maze = []
maze = [list(map(int, input())) for _ in range(n)]
# 이동방향 설정 (상,하,좌,우)
dx = [-1,1,0,0]
dy = [0,0,-1,1]


def bfs(x,y):
    q = deque()
    q.append((x,y))
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 범위 넘어가면 무시
            if nx < 0 or ny <0 or nx >= n or ny >= m:
                continue
            # 괴물 만나면 무시
            if maze[nx][ny] == 0:
                continue
            # 최단거리 기록
            if maze[nx][ny] == 1:
                maze[nx][ny] = maze[x][y] + 1
                q.append((nx,ny))
    return maze[-1][-1]


# 시작지점
print(bfs(0,0))
