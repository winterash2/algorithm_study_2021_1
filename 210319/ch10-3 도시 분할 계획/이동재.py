def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


N, M = map(int, input().split())
INF = float('inf')
graph = [[] for _ in range(N+1)]
parent = [i for i in range(N+1)]
roads = []
for _ in range(M):
    A, B, C = map(int, input().split())
    roads.append((C, A, B))
roads.sort()

answer = []
for cost, a, b in roads:
    if find(parent, a) != find(parent, b):
        union(parent, a, b)
        answer.append(cost)

answer = sum(answer) - answer[-1]
print(answer)

"""
7 12
1 2 3
1 3 2
3 2 1
2 5 2
3 4 4
7 3 6
5 1 5
1 6 2
6 4 1
6 5 3
4 5 3 
6 7 4
"""