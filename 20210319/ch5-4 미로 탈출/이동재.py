from collections import deque

N, M = map(int, input().split())
visited = [[False for _ in range(M)] for _ in range(N)]
arr = []
for _ in range(N):
    arr.append([int(x) for x in list(input().split()[0])])

# [print(x) for x in arr]

q = deque([(0,0)])

directions = [(0,1), (0,-1), (1,0), (-1,0)]
isEnd = False
depth = 0
while q:
    depth += 1
    for _ in range(len(q)):
        x, y = q.popleft()
        visited[x][y] = True
        if x == N-1 and y == M-1:
            isEnd = True
            break
        for d in directions:
            nx = x + d[0]
            ny = y + d[1]
            if 0 <= nx < N and 0 <= ny < M:
                if arr[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx, ny))
    if isEnd:
        break

print(depth)

"""
5 6
101010
111111
000001
111111
111111
"""
"""
6 6
101010
111111
000001
111111
111110
111111
"""