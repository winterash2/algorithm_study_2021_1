# http://boj.kr/1012
from collections import deque

def bfs(x, y):
    q = deque([(x, y)])
    # 상하좌우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if bchoo[nx][ny] == 1:
                    bchoo[nx][ny] = 0
                    q.append((nx, ny))
                
for _ in range(int(input())):
    m, n, k = map(int, input().split())

    bchoo = [[0] * (m) for _ in range(n)]
    
    for _ in range(k):
        i, j = map(int, input().split())
        bchoo[j][i] = 1
    cnt = 0
    for k in range(n):
        for l in range(m):
            if bchoo[k][l] == 1:
                # bfs가 실행될 때마다 cnt+1 => 배추의 집단 => 벌레의 개수
                bfs(k, l)
                bchoo[k][l] = 0
                cnt += 1

    print(cnt)
    