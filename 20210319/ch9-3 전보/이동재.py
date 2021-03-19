import heapq


def dijkstra(graph, start):
    N = len(graph) - 1
    q = [(0, start)]
    INF = float('inf')
    distances = [INF for _ in range(N+1)]
    while q:
        dist, cur = heapq.heappop(q)
        if dist >= distances[cur]:
            continue
        distances[cur] = dist
        for cost, nxt in graph[cur]:
            ndist = dist + cost
            if distances[nxt] > ndist:
                heapq.heappush(q, (ndist, nxt))
    return distances


N, M, C = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, dist = map(int, input().split())
    graph[a].append((dist, b))
INF = float('inf')

Cto = dijkstra(graph, C)
numberOfCity = 0
maxDist = 0
for i in range(1, N+1):
    if Cto[i] != INF:
        numberOfCity += 1
        maxDist = max(maxDist, Cto[i])
if numberOfCity == 1:  # 자기 자신밖에 연결된게 없는 경우
    print(0, 0)
else:
    # numberOfCity에서 -1 하는 이유는 자기 자신도 포함되어 버리기 때문
    print(numberOfCity-1, maxDist)
