import heapq


def dijkstra(distances, start):
    q = [(0, start)]
    while q:
        curr_dist, curr_hutgan = heapq.heappop(q)
        if curr_dist >= distances[curr_hutgan]:
            continue
        distances[curr_hutgan] = curr_dist
        for next_hutgan in paths[curr_hutgan]:
            heapq.heappush(q, (curr_dist+1, next_hutgan))


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

n = 6
s = 4
a = 6
b = 2
fares = [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]
print(solution(n, s, a, b, fares))


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