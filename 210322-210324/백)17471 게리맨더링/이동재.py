from itertools import combinations


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


def link_group(group):
    global graph
    global populations
    group = list(group)
    group.sort()
    parent = [i for i in range(N+1)]
    q = []
    root = group[0]
    q.append(root)
    while q:
        cur = q.pop()
        if find(parent, cur) == root and find(parent, cur) != cur:
            continue
        union(parent, cur, root)
        for nxt in graph[cur]:
            if nxt in group:
                q.append(nxt)
    count = 0
    for city in group:
        if find(parent, city) != root:
            return -1
        else:
            count += populations[city]
    return count


N = int(input())
citys = [i+1 for i in range(N)]
populations = [0] + list(map(int, input().split()))
# inp_pops = list(map(int, input().split()))
# populations = []
# for i in range(N):
#     populations.append((i+1, inp_pops[i]))
graph = [[] for _ in range(N+1)]
for i in range(1, N+1):
    graph[i] += list(map(int, input().split()))[1:]

parent = [i for i in range(N+1)]

answer = 1e9
for i in range(1, N//2+1):
    for groupA in combinations(citys, i):
        groupB = []
        for city in citys:
            if city not in groupA:
                groupB.append(city)
        countA = link_group(groupA)
        countB = link_group(groupB)
        # print(groupA, groupB, countA, countB)
        if countA == -1 or countB == -1:
            continue
        answer = min(answer, abs(countA-countB))

if answer == 1e9:
    print(-1)
else:
    print(answer)
