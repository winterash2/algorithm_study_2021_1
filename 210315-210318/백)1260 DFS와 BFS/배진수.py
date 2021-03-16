import sys
from collections import deque

n, m, start = map(int, input().split())
graph = [[] for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(now, visited):
    print(now, end=" ")
    chk = True
    for i in range(n):
        if visited[i] == 0:
            chk = False
            break

    if chk == False:
        for i in graph[now]:
            if visited[i] == 0:
                visited[i] = 1
                dfs(i, visited)


def bfs(start):
    q = deque()
    visit = [0] * (n+1)
    visit[start] = 1
    q.append(start)

    while q:
        x = q.popleft()
        print(x, end=" ")
        for i in graph[x]:
            if visit[i] == 0:
                visit[i] = 1
                q.append(i)

for i in range(1, n+1):
    graph[i].sort()

visited = [0] * (n+1)
visited[start] = 1
dfs(start, visited)
print()
bfs(start)
