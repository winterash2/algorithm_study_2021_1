import heapq


def alphaToInt(a):
    if a == '0':
        return 0
    elif 'a' <= a <= 'z':
        return ord(a) - ord('a') + 1
    elif 'A' <= a <= 'Z':
        return ord(a) - ord('A') + 27


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


N = int(input())
graph = [[] for _ in range(N)]
for i in range(N):
    graph[i] = [x for x in input()]

q = []
answer = 0

for i in range(N):
    for j in range(N):
        if i == j:
            answer += alphaToInt(graph[i][j])
        elif graph[i][j] != '0':
            q.append((alphaToInt(graph[i][j]), i, j))

parent = [i for i in range(N)]
heapq.heapify(q)

while q:
    l, a, b = heapq.heappop(q)
    if find(parent, a) != find(parent, b):
        union(parent, a, b)
    else:
        answer += l

for i in range(N):
    find(parent, i)

enable = True
for p in parent:
    if p != parent[0]:
        enable = False
        break
if enable:
    print(answer)
else:
    print(-1)


"""
3
abc
def
ghi
"""
"""
3
ABC
DEF
GHI
"""
