n, m = map(int, input().split())    
arr = []

for i in range(n):
    arr.append(list(map(int, input().split())))
# dfs이용하여 특정 노드에 연결된 모든 노드 방문
def dfs(x, y):
    if x >= n or x <= -1 or y <= 1 or y >= n:
        return False
    if arr[i][j] == 0:
        arr[i][j] = 1

        # 상,하,좌,우 재귀적으로 호출 
        dfs(i-1, j)
        dfs(i, j-1)
        dfs(i+1, j)
        dfs(i, j+1)

        return True
    return False

# 모든 위치에 댛여 음료수 채우기
result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == 1:
            result += 1

print(result)