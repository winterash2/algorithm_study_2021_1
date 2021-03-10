from collections import deque
import sys

input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]
for i in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

if n == 3:
    print(1)
else:
    visit = [0] * (n+1)
    q = deque()
    q.append(1)
    visit[1] = 1

    adapter = []
    while q:
        x = q.popleft()
        for i in graph[x]:
            if visit[i] == 0:
                visit[i] = 1
                q.append(i)
                if len(graph[i]) == 1 and x not in adapter:
                    adapter.append(i)
                elif len(graph[i]) > 1 and x not in adapter:
                    adapter.append(i)
    print(len(adapter))
