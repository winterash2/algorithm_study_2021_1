import heapq

# N, M = map(int, input().split()) # 2 <= N <= 20000, 1 <= M <= 50000
# # N, M의 크기를 봤을 떄 플로이드 워셜을 이용하여 시간 초과 날 것 같음
# # 따라서 데이크스트라 이용
# paths = [[] for _ in range(N+1)]
# for _ in range(M):
#     A, B = map(int, input().split())
#     paths[A].append(B)
#     paths[B].append(A)


def dijkstra(distances, start):
    q = [(0, start)]
    while q:
        curr_dist, curr_hutgan = heapq.heappop(q)
        if curr_dist >= distances[curr_hutgan]:
            continue
        distances[curr_hutgan] = curr_dist
        for next_hutgan in paths[curr_hutgan]:
            heapq.heappush(q, (curr_dist+1, next_hutgan))


N, M = 6, 7
paths = [[], [3, 2], [3, 1, 4, 5], [6, 4, 2, 1], [3, 2], [2], [3]]

q = [(0, 1)]

INF = float('inf')
distances = [INF for _ in range(N+1)]
dijkstra(distances, 1)

print(distances)

max_dist = 0
max_index = 0
max_count = 0
for i in range(1, N+1):
    if distances[i] != INF:
        if distances[i] > max_dist:
            max_dist = distances[i]
            max_index = i
            max_count = 1
        elif distances[i] == max_dist:
            max_count += 1

print(max_index, max_dist, max_count)
