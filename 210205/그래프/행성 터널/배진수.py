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

n = int(input())
parent = [i for i in range(n + 1)]

x_list = []
y_list = []
z_list = []
for i in range(1, n + 1):
    x, y, z = map(int,input().split())
    x_list.append((x, i))
    y_list.append((y, i))
    z_list.append((z, i))

x_list.sort()
y_list.sort()
z_list.sort()

count_list = []
for i in range(1, n):
    count_list.append((abs(x_list[i][0] - x_list[i-1][0]), x_list[i][1], x_list[i-1][1]))
    count_list.append((abs(y_list[i][0] - y_list[i-1][0]), y_list[i][1], y_list[i-1][1]))
    count_list.append((abs(z_list[i][0] - z_list[i-1][0]), z_list[i][1], z_list[i-1][1]))
count_list.sort()

res = 0
answer = 0
for co in count_list:
    cost, a, b = co
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        answer += cost
        res += 1
    if res == n:
        break

print(answer)