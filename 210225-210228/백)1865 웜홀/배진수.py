import heapq
import sys
INF = int(1e9)
input = sys.stdin.readline

testcase = int(input())

def bellman():
    for i in range(1, n+1):
        for j in range(1, n+1):
            for now, cost in graph[j]:
                if distance[now] > cost + distance[j]:
                    distance[now] = cost + distance[j]
                    if i == n:
                        return False
    return True


for _ in range(testcase):
    n, m, w = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    distance = [INF] * (n+1)

    for i in range(m):
        start, end, time = map(int, input().split())
        graph[start].append((end, time))
        graph[end].append((start, time))

    for i in range(w):
        start, end, time = map(int, input().split())
        graph[end].append((start, -time))

    answer = bellman()
    print("NO" if answer else "YES")

# 다익스트라 쓰면 시간초과 납니다.. 벨만 포트만 알고리즘 쓰세요 여러분
"""
import heapq
import sys
INF = int(1e9)
input = sys.stdin.readline

testcase = int(input())

for _ in range(testcase):
    n, m, w = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    for i in range(m):
        start, end, time = map(int, input().split())
        graph[start].append((end, time))
        graph[end].append((start, time))

    distance = [INF] * (n+1)

    def dijkstra(start):
        q = []
        heapq.heappush(q, (0, start))
        distance[start] = 0
        while q:
            dist, now = heapq.heappop(q)
            if distance[now] < dist:
                continue
            for i in graph[now]:
                cost = dist + i[1]
                if cost < distance[i[0]]:
                    distance[i[0]] = cost
                    heapq.heappush(q, (cost, i[0]))

    for i in range(w):
        end, start, time = map(int, input().split())
        dijkstra(start)
        check = False
        if distance[end] < time and distance[end] != INF:
            check = True
            print("YES")
            print(distance[end])
            break
    if check == False:
        print("NO")
"""