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
            data.append((graph[x][y], x,y,0))


data.sort()
queue = deque(data)

s, X, Y = map(int,input().split())





while queue:
    v, x, y, sec = queue.popleft()
    if sec >= s:
        break

    for i in range(4):
        
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue

        if graph[nx][ny] != 0:
            continue

        if graph[nx][ny] == 0:
            graph[nx][ny] = v 
            queue.append((v, nx, ny, sec+1))
    # 그래프 출력
    # for i in graph:
    #     print(i)
    # print("\n")
print(graph[X-1][Y-1])
