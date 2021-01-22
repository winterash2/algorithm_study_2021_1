from collections import deque

n, k = map(int, input().split())
# n, k = 3, 3
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# graph = [[1,0,2],[0,0,0],[3,0,0]]
graph = []
data = []
for x in range(n):
    graph.append(list(map(int, input().split())))
    for y in range(n):
        if graph[x][y] != 0:
            # 바이러스값(sort하기위해), 바이러스위치, 시간
            data.append((graph[x][y], x, y, 0))


# 정렬 후 큐에 삽입
data.sort()
queue = deque(data)

s, X, Y = map(int,input().split())




# bfs 이용
while queue:
    v, x, y, sec = queue.popleft()
    if sec >= s:
        break

    # 현재 위치에서 4가지 위치 각각 확인
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue

        # 방문하지 않은 위치일 경우 바이러스 전파 
        if graph[nx][ny] == 0:
            graph[nx][ny] = v 
            queue.append((v, nx, ny, sec+1))
    # 그래프 출력
    # for i in graph:
    #     print(i)
    # print("\n")
print(graph[X-1][Y-1])
