from collections import deque

T = int(input())

for _ in range(T):
    M, N, K = map(int, input().split())
    visited = [[False for _ in range(M)] for _ in range(N)]
    farm = [[False for _ in range(M)] for _ in range(N)]
    baechus = []
    q = deque()
    for _ in range(K):
        x, y = map(int, input().split())
        baechus.append((x, y))
        farm[y][x] = True
        # q.append((x, y))

    answer = 0
    for baechu in baechus:
        x, y = baechu
        if not visited[y][x]:
            q.append((x, y))
            while q:
                x, y = q.pop()
                if 0 <= x < M and 0 <= y < N and not visited[y][x] and farm[y][x]:
                    visited[y][x] = True
                    q.append((x-1, y))
                    q.append((x+1, y))
                    q.append((x, y-1))
                    q.append((x, y+1))
                else:
                    continue
            answer += 1

    print(answer)