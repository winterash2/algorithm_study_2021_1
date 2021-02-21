"""
from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
indegree = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1


def topology():
    result = []
    q = deque()
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        if now in result:
            continue
        else:
            result.append(now)
            graph[now].sort()
            for i in graph[now]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    q.append(i)

    return result


result = topology()

"""
import heapq
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
indegree = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1


def topology():
    result = []
    q = []
    for i in range(1, n+1):
        if indegree[i] == 0:
            heapq.heappush(q, i)

    while q:
        now = heapq.heappop(q)
        result.append(now)
        graph[now].sort()
        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                heapq.heappush(q, i)

    return result

result = topology()
for res in result:
    print(res, end=" ")
