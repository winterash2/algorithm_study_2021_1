import heapq

def dijkstra(distances, start):
    hq = []
    heapq.heappush(hq, (0, start))
    while hq:
        curr_time, curr_city = heapq.heappop(hq)
        if distances[curr_city] != INF:
            continue
        distances[curr_city] = curr_time
        for next_city, dist in paths[curr_city]:
            heapq.heappush(hq, (curr_time+dist, next_city))

N, M, C = map(int, input().split())
paths = [[] for _ in range(N+1)]
for _ in range(M):
    X, Y, Z = map(int, input().split())
    paths[X].append((Y, Z))

INF = float('inf')
distances = [INF for _ in range(N+1)]

dijkstra(distances, C)
number_of_city = 0
max_dist = 0
for dist in distances:
    if dist == INF:
        continue
    else:
        number_of_city += 1
        max_dist = max(max_dist, dist)

print(number_of_city-1, max_dist)

"""
3 2 1
1 2 4
1 3 2
"""
