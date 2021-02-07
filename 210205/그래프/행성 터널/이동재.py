import sys
input = sys.stdin.readline

N = int(input())
planets = []
for _ in range(N):
    x, y, z = map(int, input().split())
    planets.append((x, y, z))

roads = []
for i in range(N):
    for j in range(i+1, N):
        min_len = min(
            abs(planets[i][0] - planets[j][0]),
            abs(planets[i][1] - planets[j][1]),
            abs(planets[i][2] - planets[j][2]))
        roads.append((i, j, min_len))

roads.sort(key=lambda x: x[2])


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


parent = [i for i in range(N)]

total_len = 0
for a, b, l in roads:
    if find(parent, a) != find(parent, b):
        total_len += l
        union(parent, a, b)

print(total_len)

"""
5 
11 -15 -15
14 -5 -15
-1 -1 -5
10 -4 -1
19 -4 19
"""
