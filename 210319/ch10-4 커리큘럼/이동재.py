N = int(input())
lectures = []
costs = [0]
graph = [[] for _ in range(N+1)]
degrees = [0 for _ in range(N+1)]
for i in range(N):
    line = list(map(int, input().split()))[:-1]
    costs.append(line[0])
    for need in line[1:]:
        degrees[i+1] += 1
        graph[need].append(i+1)

q = []
for i in range(1, N+1):
    if degrees[i] == 0:
        q.append((0, i)) # (시작 시간, 강의 번호)

result = [0 for _ in range(N+1)]
while q:
    for _ in range(len(q)):
        dist, cur = q.pop()
        result[cur] = dist + costs[cur]
        for nxt in graph[cur]:
            degrees[nxt] -= 1
            if degrees[nxt] == 0:
                q.append((dist + costs[cur], nxt))

[print(x) for x in result[1:]]

"""
5
10 -1
10 1 -1
4 1 -1
4 3 1 -1
3 3 -1
"""