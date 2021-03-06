import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
degrees = [0 for _ in range(N+1)]
for _ in range(M):
    A, B = map(int, input().split())
    graph[B].append(A)
    degrees[A] += 1

q = []
for i in range(1, N+1):
    if degrees[i] == 0:
        q.append(i)

result = []
while q:
    cur = q.pop()
    result.append(cur)
    for elem in graph[cur]:
        degrees[elem] -= 1
        if degrees[elem] == 0:
            q.append(elem)
result = result[::-1]

for elem in result:
    print(elem, end=" ")

"""
import heapq

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
degrees = [0 for _ in range(N+1)]
for _ in range(M):
    A, B = map(int, input().split())
    graph[B].append(A)
    degrees[A] += 1

q = []
for i in range(1, N+1):
    if degrees[i] == 0:
        q.append(i)
heapq.heapify(q)

result = []
while q:
    cur = heapq.heappop(q)
    result.append(cur)
    for elem in graph[cur]:
        degrees[elem] -= 1
        if degrees[elem] == 0:
            heapq.heappush(q, elem)
result = result[::-1]

for elem in result:
    print(elem, end=" ")
"""