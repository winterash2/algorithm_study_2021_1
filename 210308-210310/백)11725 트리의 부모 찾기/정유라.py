# http://boj.kr/11725
from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
# print(graph)

visited = [False] * (n+1)
q = deque(graph[1])
visited[1] = True
tree = [0] * (n+1)
while q:
    now = q.popleft()
    visited[now] = True

    for i in graph[now]:
        if not visited[i]:
            tree[i] = now
            q.append(i)

for i in range(2, n+1):
    if tree[i] == 0:
        print(1)
    else:
        print(tree[i])