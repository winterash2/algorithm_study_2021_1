from collections import deque

n, l, r = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))


dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

result = 0

# bfs 이용
# 특정 위치에서 출발하여 모든 연합을 체크한 뒤에 데이터 갱신
def check_union(x, y, index):
    united = []
    united.append((x,y))

    q = deque()
    q.append((x,y))
    union[x][y] = index # 현재 연합의 번호 할당
    total = graph[x][y] # 현재 연합의 전체 인구 수
    count = 1 # 현재 연합의 국가 수

    # 큐를 돌면서 반복
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and union[nx][ny] == -1:
                if l <= abs(graph[nx][ny] - graph[x][y]) <= r:
                    q.append((nx, ny))

                    # 연합에 추가
                    union[x][y] = index
                    total += graph[nx][ny]
                    count += 1
                    united.append((nx, ny))
    
    # 연합된 나라끼리 인구 분배
    for i, j in united:
        graph[i][j] = total // count
    return count


total_count = 0

# 더 이상 인구 분배 불가능할 때까지 반복
while True:
    union = [[-1] * n for _ in range(n)]
    index = 0
    for i in range(n):
        for j in range(n):
            if union[i][j] == -1:
                check_union(i, j, index)
                index += 1
    if index == n * n:
        break
    total_count += 1

print(total_count)