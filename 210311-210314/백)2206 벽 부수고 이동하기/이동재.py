# 3차 시도
# 성공은 했는데 진수가 훨 빠름, 진수의 설명을 들어볼 것
from collections import deque
import heapq
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append([int(x) for x in input().split()[0]])

visited = [[[False, False] for _ in range(M)] for _ in range(N)]
q = deque()
q.append((0, 0, 1, False)) # x, y, distance, 벽 넘었는지
answer = 1e9
while q:
    x, y, distance, broke = q.popleft()

    if broke == True: # 벽을 부순 적이 있으면
        if visited[x][y][1] == True:
            continue
        visited[x][y][1] = True
    else: # 벽을 부순 적이 없으면
        if visited[x][y][0] == True:
            continue
        visited[x][y][0] = True

    if x == N-1 and y == M-1:
        answer = min(answer, distance)

    for d in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx = x + d[0]
        ny = y + d[1]
        if 0 <= nx < N and 0 <= ny < M:
            if graph[nx][ny] == 1: # 벽이면
                if not broke: # 벽을 부순 적이 없으면
                    q.append((nx, ny, distance+1, True))
            else: # 벽이 아니면
                q.append((nx, ny, distance+1, broke))

if answer == 1e9:
    print(-1)
else:
    print(answer)


# 2차. 먼저 벽 안 뚫었을 때 돌면서 한 번 박았을 때를 기억해뒀다가
# 다 돌고 난 후에 한 번 박은 곳부터 다시 채워나가는 식으로 함
# 시간초과 뜸
"""
from collections import deque
import heapq
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append([int(x) for x in input().split()[0]])


dp = [[1e9 for _ in range(M)] for _ in range(N)]
q = deque()
q.append((0, 0))
depth = 0
qDict = dict()
while q:
    depth += 1
    for _ in range(len(q)):
        x, y = q.popleft()
        if x < 0 or x >= N or y < 0 or y >= M or dp[x][y] != 1e9:
            continue
        if graph[x][y] == 1:
            for d in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx = x + d[0]
                ny = y + d[1]
                if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] == 0:
                    if (nx, ny) not in qDict:
                        qDict[(nx, ny)] = depth + 1
            continue
        dp[x][y] = depth
        for d in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx = x + d[0]
            ny = y + d[1]
            if 0 <= nx < N and 0 <= ny < N:
                q.append((nx, ny))
answer = dp[N-1][M-1]

q = []
for key in qDict.keys():
    x, y = key
    q.append((qDict[key], x, y))

dp = [[1e9 for _ in range(M)] for _ in range(N)]
heapq.heapify(q)
while q:
    depth, x, y = heapq.heappop(q)
    dp[x][y] = depth
    for d in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx = x + d[0]
        ny = y + d[1]
        if 0 <= nx < N and 0 <= ny < M and dp[nx][ny] == 1e9 and graph[nx][ny] == 0:
            heapq.heappush(q, (depth+1, nx, ny))

answer = min(answer, dp[N-1][M-1])
if answer == 1e9:
    print(-1)
else:
    print(answer)
"""


# 1차 시도. 벽을 하나씩 없애고 전부 다시 구하는 방식
# 시간초과됨
"""
from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append([int(x) for x in input().split()[0]])


def calc(graph):
    dp = [[0 for _ in range(M)] for _ in range(N)]
    q = deque()
    q.append((0, 0))
    depth = 0
    while q:
        depth += 1
        for _ in range(len(q)):
            x, y = q.popleft()
            if x < 0 or x >= N or y < 0 or y >= M:
                continue
            if dp[x][y] != 0 or graph[x][y] == 1:
                continue
            # print(x, y)
            dp[x][y] = depth
            q.append((x-1, y))
            q.append((x+1, y))
            q.append((x, y-1))
            q.append((x, y+1))

    if dp[N-1][M-1] == 0:
        return 1e9
    else:
        return dp[N-1][M-1]


answer = 1e9
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            graph[i][j] = 0
            answer = min(answer, calc(graph))
            graph[i][j] = 1

if answer == 1e9:
    print(-1)
else:
    print(answer)
"""
