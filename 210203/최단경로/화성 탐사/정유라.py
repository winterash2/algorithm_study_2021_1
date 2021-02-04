import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

t = int(input())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for i in range(t):
    n = int(input())
    graph = []
    for j in range(n):
        graph.append(list(map(int, input().split())))
    
    distance = [[INF] * n for _ in range(n)]
    
    q = []
    x, y = 0, 0
    heapq.heappush(q, (graph[x][y], x, y)) # 시작노드로 가기 위한 비용은 (0, 0)위치의 값

    while q:
        dist, x, y = heapq.heappop(q)

        if distance[x][y] < dist:
            continue
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 범위
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            cost = dist + graph[nx][ny]
            
            if cost < distance[nx][ny]:
                distance[nx][ny] = cost
                heapq.heappush(q, (cost, nx, ny))
    print(distance[n-1][n-1])        
    
