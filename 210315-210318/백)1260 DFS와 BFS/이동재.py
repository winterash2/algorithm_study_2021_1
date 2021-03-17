from collections import deque

N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for g in graph:
    g.sort()


def dfs(cur):
    global visited, answerDFS, graph
    if visited[cur]:
        return
    visited[cur] = True
    answerDFS.append(cur)
    for nxt in graph[cur]:
        dfs(nxt)


visited = [False for _ in range(N+1)]
answerDFS = []
dfs(V)

q = deque([V])
visited = [False for _ in range(N+1)]
answerBFS = []
while q:
    cur = q.popleft()
    if visited[cur]:
        continue
    visited[cur] = True
    answerBFS.append(cur)
    for nxt in graph[cur]:
        q.append(nxt)

for elem in answerDFS:
    print(elem, end=' ')
print()
for elem in answerBFS:
    print(elem, end=' ')

