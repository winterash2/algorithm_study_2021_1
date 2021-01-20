n, m = map(int, input().split())    
arr = []

for i in range(n):
    arr.append(list(map(int, input().split())))

def dfs(x, y):
    if x >= n or x <= -1 or y <= 1 or y >= n:
        return False
    if arr[i][j] == 0:
        arr[i][j] = 1
        dfs(i-1, j)
        dfs(i, j-1)
        dfs(i+1, j)
        dfs(i, j+1)

        return True
    return False

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == 1:
            result += 1

print(result)