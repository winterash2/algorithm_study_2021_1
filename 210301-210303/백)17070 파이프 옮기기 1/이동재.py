N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

dpG = [[0 for _ in range(N+1)] for _ in range(N+1)] # dp 가로
dpS = [[0 for _ in range(N+1)] for _ in range(N+1)] # dp 세로
dpD = [[0 for _ in range(N+1)] for _ in range(N+1)] # dp 대각선
dpG[1][2] = 1

for r in range(1, N+1):
    for c in range(1, N+1):
        if graph[r-1][c-1] == 0:
            dpG[r][c] += dpG[r][c-1]
            dpG[r][c] += dpD[r][c-1]
            dpS[r][c] += dpS[r-1][c]
            dpS[r][c] += dpD[r-1][c]
            if graph[r-2][c-1] == 0 and graph[r-1][c-2] == 0:
                dpD[r][c] += dpG[r-1][c-1]
                dpD[r][c] += dpS[r-1][c-1]
                dpD[r][c] += dpD[r-1][c-1]

print(dpG[N][N] + dpS[N][N] + dpD[N][N])


# 아래랑 똑같이 풀고 있었음...
# 넣기 전에 확인한다는 것만 다름 
"""
from collections import deque

N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

# 가로 1, 세로 2, 대각선 3
# 처음에는 (0,0), (0,1) 가로
qPrev = []
q = []
qPrev.append([1, 0, 1])
answer = 0
while qPrev:
    for pipe in qPrev:
        # print(pipe)
        if pipe[1] == N-1 and pipe[2] == N-1:
            answer += 1
            continue

        if pipe[0] == 1:  # 가로일 때
            # 가로로 보낼 때
            if pipe[2] + 1 < N and graph[pipe[1]][pipe[2] + 1] == 0:
                q.append([1, pipe[1], pipe[2] + 1])
            # 대각선으로 보낼 때
            if pipe[1] + 1 < N and pipe[2] + 1 < N:
                if graph[pipe[1]+1][pipe[2]] == 0 and graph[pipe[1]][pipe[2]+1] == 0 and graph[pipe[1]+1][pipe[2]+1] == 0:
                    q.append([3, pipe[1] + 1, pipe[2] + 1])
        elif pipe[0] == 2:  # 세로일 때
            # 세로로 보낼 때
            if pipe[1] + 1 < N and graph[pipe[1]+1][pipe[2]] == 0:
                q.append([2, pipe[1]+1, pipe[2]])
            # 대각선으로 보낼 때
            if pipe[1] + 1 < N and pipe[2] + 1 < N:
                if graph[pipe[1]+1][pipe[2]] == 0 and graph[pipe[1]][pipe[2]+1] == 0 and graph[pipe[1]+1][pipe[2]+1] == 0:
                    q.append([3, pipe[1] + 1, pipe[2] + 1])
        else:
            # 가로로 보낼 때
            if pipe[2] + 1 < N and graph[pipe[1]][pipe[2] + 1] == 0:
                q.append([1, pipe[1], pipe[2] + 1])
            # 세로로 보낼 때
            if pipe[1] + 1 < N and graph[pipe[1]+1][pipe[2]] == 0:
                q.append([2, pipe[1]+1, pipe[2]])
            # 대각선으로 보낼 때
            if pipe[1] + 1 < N and pipe[2] + 1 < N:
                if graph[pipe[1]+1][pipe[2]] == 0 and graph[pipe[1]][pipe[2]+1] == 0 and graph[pipe[1]+1][pipe[2]+1] == 0:
                    q.append([3, pipe[1] + 1, pipe[2] + 1])
    qPrev = q
    q = []

print(answer)
"""

# deque를 이용해서 bfs
"""
from collections import deque

N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

# 가로 1, 세로 2, 대각선 3
# 처음에는 (1,1), (1,2) 가로
visited = []
pipe = [1, [0, 0], [0, 1]]
q = deque()
q.append(pipe)
answer = 0
while q:
    for _ in range(len(q)):
        pipe = q.popleft()
        shape, left, right = pipe

        if right[0] >= N or right[1] >= N:
            continue
        # if graph[left[0]][left[1]] == 1 or graph[right[0]][right[1]] == 1:
        if graph[right[0]][right[1]] == 1:
            continue
        if shape == 3:
            if graph[left[0]][left[1]+1] == 1 or graph[left[0]+1][left[1]] == 1:
                continue

        if right[0] == N-1 and right[1] == N-1:
            answer += 1
            continue

        if shape == 1:  # 가로 방향
            # 가로로 오른쪽으로 감
            q.append([1, right, [right[0], right[1]+1]])
            # 대각선으로 내려감
            q.append([3, right, [right[0]+1, right[1]+1]])
        elif shape == 2:  # 세로 방향
            # 세로로 내려감
            q.append([2, right, [right[0]+1, right[1]]])
            # 대각선으로 내려감
            q.append([3, right, [right[0]+1, right[1]+1]])
        else:  # 대각선 방향
            # 가로로 오른쪽으로 감
            q.append([1, right, [right[0], right[1]+1]])
            # 세로로 내려감
            q.append([2, right, [right[0]+1, right[1]]])
            # 대각선으로 내려감
            q.append([3, right, [right[0]+1, right[1]+1]])

print(answer)
"""
