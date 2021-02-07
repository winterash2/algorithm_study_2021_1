# 서로소집합 알고리즘

gate = int(input())
plane = int(input())

# 부모 찾기
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 합치기
def union(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 초기화
parent = [0] * (gate+1)
for i in range(1, gate+1):
    parent[i] = i


result = 0
for i in range(plane):
    data = int(input())
    data_root = find_parent(parent, data)
    if data_root == 0:
        break
    union(parent, data_root, data_root-1)
    result += 1

print(result)


# for i in range(plane):
#     data = int(input())
      # 입력받은 게이트번호부터 역순으로 반복문 돌면서 확인해서 루트 다르면 union해주려고 했는데 한번에 다 처리해서 fail.. 
#     for d in range(data, 0, -1):          
#         if find_parent(parent, d) != find_parent(parent, d-1):
#             union(parent, d, d-1)