import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

n, m, start = map(int, input().split()) 

# 초기화 
distance = [INF] * (n+1) 
# visited = [INF] * (n+1)
graph = [[] for _ in range(n+1)]
for i in range(m):
    x, y, message_time = map(int, input().split())
    graph[x].append((y, message_time))


def daikjstra(start):
    distance[start] = 0
    # visited[start] = True
    q = []
    heapq.heappush(q, (0, start))


    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue


        for j in graph[now]:
            cost = distance[now] + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost
                heapq.heappush(q, (cost, j[0]))

    # for j in graph[start]:
    #     distance[j[0]] = j[1]

    # for i in range(n-1):
    #     now = get_smallest_node()
    #     visited[now] = True

    #     for j in graph[now]:
    #         cost = distance[now] + j[1]
    #         if cost < distance[j[0]]:
    #             distance[j[0]] = cost
    
daikjstra(start)
count = 0
max_m_time = -1e9
for i in range(1, n+1):
    if distance[i] != INF and i != start:
        count += 1
        max_m_time = max(distance[i], max_m_time)
            
print(count, max_m_time)