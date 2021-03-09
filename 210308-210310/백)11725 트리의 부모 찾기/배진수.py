from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
graph = [[] for i in range(n+1)]
parent = [0] * (n+1)

for i in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

q = deque()
q.append(1)

while q:
    x = q.popleft()
    for i in graph[x]:
        if parent[i] == 0:
            parent[i] = x
            q.append(i)

for child in parent[2:]:
    print(child)