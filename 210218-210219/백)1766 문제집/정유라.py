# http://boj.kr/1766
# 힙을 이용한 위상 정렬 알고리즘 
import heapq

v, e = map(int, input().split())

indegree = [0] * (v+1)

graph = [[] for i in range(v+1)]

for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)

    indegree[b] += 1
    

def topology_sort():
    result = []
    q = []
    for i in range(1, v+1):
        if indegree[i] == 0:
            heapq.heappush(q, i)

    while q:
        now = heapq.heappop(q)
        result.append(now)

        for i in graph[now]:
            indegree[i] -= 1

            if indegree[i] == 0:
                heapq.heappush(q, i)
    # for i in result:
    #     print(i, end=" ")
    print(*result)
topology_sort()