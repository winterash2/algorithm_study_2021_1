import heapq
import sys

input = sys.stdin.readline
INF = 1e9

n, m, c = map(int, input().split())
graph = [[] for _ in range(n + 1)]
distance = [INF] * (n+1)

for _ in range(n+1):
    x, y, z = map(int, input().split())
    graph[x].append(y, z)

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(c)

count = 0
long_time = 0
for d in distance:
    if d != INF:
        count += 1
        long_time = max(long_time, d)

print(count-1, long_time)

