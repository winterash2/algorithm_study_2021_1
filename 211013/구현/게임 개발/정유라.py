n, m = map(int, input().split())    
x, y, current_direction = map(int, input().split())

# 방문한 위치를 저장하기 위한 맵 생성
d = [[0]*m for _ in range(n)]
d[x][y] = 1
# 전체 맵 정보 입력받기
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

count = 1
turn_time = 0

while True:
    # turn left
    current_direction = (current_direction+1)%4

    nx = x + dx[current_direction]
    ny = y + dy[current_direction]
    if d[nx][ny] == 0 and array[nx][ny] != 1:
        x, y = nx, ny
        d[nx][ny] = 1
        count += 1
        turn_time = 0
        continue
    else:
        turn_time += 1
    
    if turn_time == 4:
        nx = x - dx[current_direction]
        ny = y - dy[current_direction]
        if array[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turn_time = 0

print(count)
