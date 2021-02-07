import sys
input = sys.stdin.readline


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n, m = map(int, input().split())

travel = []
for i in range(n):
    arr = list(map(int, input().split()))
    travel.append(arr)

result = list(map(int, input().split()))

parent = [i for i in range(n)]

for i in range(n):
    for j in range(n):
        if travel[i][j] == 1:
            union_parent(parent, i, j)

temp = parent[result[0] - 1]
answer = "YES"
for res in result:
    if parent[res-1] == temp:
        continue
    else:
        answer = "NO"
        break

print(answer)
