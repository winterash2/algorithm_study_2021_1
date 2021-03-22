import heapq

def dijkstra(graph, start, n):
    distances = [1e9] * (n+1)
    q = []
    heapq.heappush(q, (0, start))
    while q:
        dist, now = heapq.heappop(q)
        if distances[now] <= dist:
            continue
        distances[now] = dist
        for nxt in graph[now]:
            cost = dist + nxt[1]
            if cost < distances[nxt[0]]:
                heapq.heappush(q, (cost, nxt[0]))
    return distances


def solution(n, s, a, b, fares):
    answer = 0
    graph = [[] for _ in range(n+1)]
    for i, j, dist in fares:
        graph[i].append((j, dist))
        graph[j].append((i, dist))
    sTo = dijkstra(graph, s, n)
    answer = 1e9
    for k in range(1, n+1):
        kTo = dijkstra(graph, k, n)
        answer = min(answer, sTo[k] + kTo[a] + kTo[b])
    return answer

n = 6
s = 4
a = 6
b = 2
fares = [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]
print(solution(n, s, a, b, fares))


# 플로이드 워셜로 한 것, 효율성 딱 한 개 빼고 만족함
"""
def solution(n, s, a, b, fares):
    answer = 0
    floyd = [[1e9 for _ in range(n+1)] for _ in range(n+1)]
    for i in range(1, n+1):
        floyd[i][i] = 0
    for i, j, dist in fares:
        floyd[i][j] = dist
        floyd[j][i] = dist
    
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                floyd[i][j] = min(floyd[i][j], floyd[i][k] + floyd[k][j])

    answer = 1e9
    for k in range(1, n+1):
        answer = min(answer, floyd[s][k] + floyd[k][a] + floyd[k][b])

    return answer
"""