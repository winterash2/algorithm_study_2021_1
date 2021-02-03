## 다익스트라
import heapq

INF = int(1e9)
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)


for i in range(m):
    a, b = map(int, input().split())
    graph[a].append((b, 1))
    graph[b].append((a, 1))



def dijkstra(start):
    q = []

    # 시작노드 start = 1
    heapq.heappush(q, (0, 1))
    distance[1] = 0

    while q:
        dist, now = heapq.heappop(q)
        
        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(1)
result = []
count = 0
max_d = 0
index = 1e9
for i in range(1, n+1):
    if distance[i] != INF and distance[i] != 0:
        if max_d == distance[i]:
            count += 1
            index = min(index, i)
        else:
            max_d = max(max_d, distance[i])
print(distance)
print(index+1, max_d, count)
# 없는 0번째 인덱스는 제외해야함
"""
6 7        
3 6
4 3
3 2
1 3
1 2
2 4
5 2
"""