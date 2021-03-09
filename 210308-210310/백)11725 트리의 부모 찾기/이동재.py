from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
# N <= 100,000 이므로 재귀로 풀기엔 조금 그럼
graph = [[]for _ in range(N+1)]
for _ in range(N-1):
    u,v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

parent = [0 for _ in range(N+1)]
parent[1] = 1

q = deque()
q.append(1)
while q:
    cur = q.popleft()
    for f in graph[cur]:
        if parent[f] == 0:
            parent[f] = cur
            q.append(f)

[print(x) for x in parent[2:]]