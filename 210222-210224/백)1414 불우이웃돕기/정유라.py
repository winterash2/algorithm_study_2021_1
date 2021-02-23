# http://boj.kr/1414
# ... 답은 맞는데 뭘 더해야되는데 그게 뭔지 몰겟

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

# 초기화
v = int(input())
graph = [[] for _ in range(v)]
for i in range(v):
    graph[i] = [x for x in input()]

# graph = []
# for i in range(v):
#     graph.append(list(input()))

# 모든 간선을 담을 리스트와 최종 비용을 담을 변수
edges = []
result = 0

# 부모 테이블 초기화
parent = [0] * (v)
for i in range(v):
    parent[i] = i
# a-z 96 
# A-Z 38
# 97 122
# 65 90
total = 0
# 간선 정보 초기화
for i in range(v):
    for j in range(v):
        cost = graph[i][j]
        print("cost:", cost)
        if 'a' <= cost <= 'z':
            convert_cost = ord(cost) - 96
            total += convert_cost
        if 'A' <= cost <= 'Z':
            convert_cost = ord(cost) - 38
            total += convert_cost
        if cost == 0 or i == j:
            continue
        edges.append((convert_cost, i, j))

# 간선을 비용순으로 정렬
edges.sort()
print("edge", edges)
mst = []
for edge in edges:
    cost, a, b = edge
    
    # 사이클 확인
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
        mst.append(edge)

    if len(mst) == v-1:
        break

if len(mst) < v-1:
    print(-1)
else:
    print(total - result)