# bfs 이용 (미로탈출 참고)

# 1. 초기화 -1로 안 하고 0으로 해서 거리 계산 틀림
# 2. 무조건 맨위, 왼쪽인 줄 알고 최소거리 계산 안 해서 틀림

from collections import deque

n = int(input())
x, y = 0, 0
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j] == 9:
            x, y = i, j
            graph[i][j] = 0

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
me = 2
growing = 0
def bfs(x, y):
    graph2 = []
    for i in range(n):
        graph2.append([-1] * n)
    graph2[x][y] = 0
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if graph[nx][ny] > me:
                continue
            if graph2[nx][ny] == -1:            
                graph2[nx][ny] = graph2[x][y] + 1
                queue.append((nx, ny))
                
            
    return graph2
total_time = 0
eat_fish_x, eat_fish_y = x, y
while True:
    after_one_step_bfs = bfs(eat_fish_x, eat_fish_y)

    min_dist = 1e9
    for i in range(n):
        for j in range(n):
            if after_one_step_bfs[i][j] != -1 and graph[i][j] < me and graph[i][j] >= 1: # 갈 수 있고, 물고기가 나보다 작을 때, 먹을수 있는 물고기일때.. 1이상
                if min_dist > after_one_step_bfs[i][j]:
                    min_dist = after_one_step_bfs[i][j]
                    eat_fish_x, eat_fish_y = i, j

    if min_dist == 1e9:
        print(total_time)
        break
    else:
        graph[eat_fish_x][eat_fish_y] = 0 # 먹었으니 0 처리
    
        total_time += after_one_step_bfs[eat_fish_x][eat_fish_y]
        growing += 1
        if me == growing:  # 이거 내 코드에서 갓동빈코드처럼 >= 하면 틀렸습니다 뜨던데 왜그렇지..?
            me += 1
            growing = 0
        


    


"""
4
4 3 2 1
0 0 0 0
0 0 9 0
1 2 3 4
"""