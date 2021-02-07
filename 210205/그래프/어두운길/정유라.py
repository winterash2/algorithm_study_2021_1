# 최소 신장 트리
# 크루스칼 알고리즘

# 부모 루트 찾기
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n, m = map(int, input().split())
parent = [0] * (n)

# 부모 자기 자신으로 초기화
for i in range(n):
    parent[i] = i

# 간선 정보 입력 받기
edges = []
for i in range(m):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))
edges.sort() # 최소 비용을 위한 오름차순 정렬

total = 0 # 총 비용
result = 0 # 최소 비용
for edge in edges:
    cost, a, b = edge
    total += cost
    if find_parent(parent, a) != find_parent(parent, b): # 부모가 다를때 = 사이클이 발생하지 않을 때 
        union_parent(parent, a, b) # 집합에 추가
        result += cost

print(total - result)

"""
7 11
0 1 7
0 3 5
1 2 8
1 3 9
1 4 7
2 4 5
3 4 15
3 5 6
4 5 8
4 6 9
5 6 11
"""