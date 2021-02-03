import sys
import heapq
input = sys.stdin.readline

INF = int(1e9)

n, m = map(int, input().split())

hide = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    hide[a].append((b,1))
    hide[b].append((a,1))
    
start = 1
def dijkstra(start):
    distance[start] = 0
    q = []
    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]:
            continue
        for i in hide[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

arr = distance[1:]
max_res = max(arr)
count = 0
result = n
for i in range(1, n+1):
    if distance[i] == max_res:
        count += 1
        result = min(result, i)
print(result, distance[result], count)
