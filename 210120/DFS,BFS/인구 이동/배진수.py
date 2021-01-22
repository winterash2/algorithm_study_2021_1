n, l, r = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]

visited = []
# 상하좌우
dx = [-1,1,0,0]
dy = [0,0,-1,1]
cal = []
count = 0

def check_move():
    for x in range(n):
        for y in range(n):
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0<= nx < n and 0<= ny < n:
                    if l <= abs(data[nx][ny] - data[x][y]) <= r:
                        return True
    return False

def dfs(x, y, arr):
    global data, visited, n, l, r, cal,count

    if check_move is True:
        count += 1
    elif check_move is not True:
        return count
    
    
    
    

arr = set()
arr.add(data[0][0])
dfs(0, 0, arr)