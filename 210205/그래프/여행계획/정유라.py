# 서로소집합 알고리즘
# 모든 도시가 같은 집합 안에 있으면 여행 가능
"""
5 4
0 1 0 1 1
1 0 1 1 0
0 1 0 0 0
1 1 0 0 0
1 0 0 0 0
2 3 4 3
"""
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
parent = [0] * (n+1)

# 부모 노드 자기 자신으로 초기화
for i in range(1, n+1):
    parent[i] = i

input_data = []

for i in range(n):
    # print("i",i)
    data = list(map(int, input().split()))
    input_data.append(data)

city = list(map(int, input().split()))
for i in range(n):
    for j in range(n): # for j in range(i+1, n): 양방향 그래프니까 이렇게 하면 절반으로 줄일 수 있다
        if input_data[i][j] == 1:
            union_parent(parent, i+1, j+1)

# 맨 첫번째 root랑 다르면 같은 그룹이 아니므로 NO            
tmp = find_parent(parent, city[0])
result = "YES"
for i in range(1, len(city)):
    if find_parent(parent, i) != tmp:
        result = "NO"
        break
print(result)
