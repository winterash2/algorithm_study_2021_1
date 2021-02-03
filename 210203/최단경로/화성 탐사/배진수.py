import sys
import heapq

input = sys.stdin.readline

INF = int(1e9)
dx = [0,0,1,-1]
dy = [1,-1,0,0]

n = int(input())

space = []
distance = [[INF]*n for _ in range(n)]

for _ in range(n):
    input_list = list(map(int, input().split()))
    space.append(input_list)

q = []
x, y = 0, 0
distance[x][y] = space[x][y]
heapq.heappush(q, (space[x][y], x, y))

while q:
    dist, x, y = heapq.heappop(q)
    if dist > distance[x][y]:
        continue

    for i in range(4):
        mx = x + dx[i]
        my = y + dy[i]
        if 0 <= mx < n and 0 <= my < n:
            cost = dist + space[mx][my]
            if cost < distance[mx][my]:
                distance[mx][my] = cost
                heapq.heappush(q, (distance[mx][my], mx, my))

print(distance[-1][-1])
# print(distance)