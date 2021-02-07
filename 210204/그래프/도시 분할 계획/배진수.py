import sys
input = sys.stdin.readline

def find_parent(parent, a):
    if parent[a] != a:
        parent[a] = find_parent(parent, parent[a])
    return parent[a]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, input().split())
parent = [i for i in range(n+1)]

citys = []
for i in range(m):
    a, b, cost = map(int, input().split())
    citys.append((cost, a, b))

citys.sort()
res = 0
cnt = 1
for city in citys:
    cost, a, b = city
    if cnt == n - 1:
        break
    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent, a, b)
        res += cost
        cnt += 1

print(res)
# print(parent)