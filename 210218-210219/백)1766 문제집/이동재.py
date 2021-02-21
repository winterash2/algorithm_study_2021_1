import heapq

N, M = map(int, input().split())
indegree = [0 for i in range(N+1)]
graph = [[] for _ in range(N+1)]

for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    indegree[B] += 1

q = []
for i in range(1, N+1):
    if indegree[i] == 0:
        heapq.heappush(q, i)

answer = []
while q:
    cur = heapq.heappop(q)
    answer.append(cur)
    for nxt in graph[cur]:
        indegree[nxt] -= 1
        if indegree[nxt] == 0:
            heapq.heappush(q, nxt)

for a in answer:
    print(a, end=" ")