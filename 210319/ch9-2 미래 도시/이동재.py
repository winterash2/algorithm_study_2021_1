N, M = map(int, input().split())
INF = float('inf')
floyd = [[INF for _ in range(N+1)] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    floyd[a][b] = 1
    floyd[b][a] = 1
for i in range(1, N+1):
    floyd[i][i] = 0
X, K = map(int, input().split())

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            floyd[i][j] = min(floyd[i][j], floyd[i][k] + floyd[k][j])

answer = floyd[1][K] + floyd[K][X]
if answer == INF:
    print(-1)
else:
    print(answer)

"""
5 7
1 2
1 3
1 4
2 4
3 4
3 5
4 5
4 5
"""

# 다익스트라로 풀기
"""
import heapq
INF = float('inf')

def dijkstra(graph, start):
    N = len(graph) - 1
    distances = [INF for _ in range(N+1)]
    q = [(0, start)] # (dist, node)
    distances[start] = 0
    while q:
        dist, cur = heapq.heappop(q)
        if distances[cur] < dist:
            continue
        distances[cur] = dist
        for nxt in graph[cur]:
            if dist + 1 < distances[nxt]:
                heapq.heappush(q, (dist + 1, nxt))
    return distances


N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
X, K = map(int, input().split())
Sto = dijkstra(graph, 1)
Kto = dijkstra(graph, K)
answer = Sto[K] + Kto[X]
if answer == INF:
    print(-1)
else:
    print(answer)
"""