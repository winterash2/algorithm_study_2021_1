# http://boj.kr/1520
def dfs(x, y):
    if x == n-1 and y == m-1:
        return 1
    if visited[x][y] == -1:
        visited[x][y] = 0

        dx = [1, -1, 0, 0]
        dy = [0, 0, -1, 1]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] < graph[x][y]:
                    visited[x][y] += dfs(nx, ny)
    return visited[x][y]
    

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))   
visited = [[-1] * m for _ in range(n)]



print(dfs(0, 0))
print(visited)


# -----------------
# def dfs(x, y):
#     global cnt, visited, n, m

#     if x == n-1 and y == m-1:
#         cnt += 1
#         visited = [[-1] * m for _ in range(n)]
#         return
    
#     dx = [1, 0, 0]
#     dy = [0, -1,1]

#     for i in range(3):
#         nx = x + dx[i]
#         ny = y + dy[i]

#         if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == -1:
#             if graph[nx][ny] < graph[x][y]:
#                 visited[nx][ny] = 1          
#                 dfs(nx, ny)
    

# n, m = map(int, input().split())
# graph = []
# for _ in range(n):
#     graph.append(list(map(int, input().split())))   
# cnt = 0    
# visited = [[-1] * m for _ in range(n)]
# dfs(0, 0)
# print(cnt)