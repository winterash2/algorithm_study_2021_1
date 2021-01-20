from collections import deque

N, K = map(int, input().split())
graph = []
for _ in range(N):
    # list(map(int, input().split())) 여기서 list()로 안 묶어서 type에러가 떴었음
    # 기본적으로 list처럼 동작은 하는데 한 개만 들어왔을 떄는 얘기가 다른가봄
    graph.append(list(map(int, input().split())))
S, X, Y = map(int, input().split())


q_all = [[] for _ in range(S+2)]
for x in range(N):
    for y in range(N):
        if graph[x][y] != 0:
            q_all[0].append((graph[x][y], x, y))
q_all[0].sort()

graph = [[0 for _ in range(N)] for _ in range(N)]  # 그래프 초기화

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

second = 0
for q in q_all:
    if second == S+1:
        break
    for virus in q:
        spec, x, y = virus
        if x < 0 or x >= N or y < 0 or y >= N:
            continue
        elif graph[x][y] == 0:
            graph[x][y] = spec
            for d in directions:
                q_all[second+1].append((spec, x+d[0], y+d[1]))
    second += 1

print(graph[X-1][Y-1])
