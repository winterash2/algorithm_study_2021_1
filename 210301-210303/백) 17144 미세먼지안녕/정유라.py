# http://boj.kr/17144
from collections import deque

r, c, t = map(int, input().split())
air = []
q = deque()      # 먼지 있는 자리
air_control = [] # 공기청정기

# 초기화
for i in range(r):
    air.append(list(map(int, input().split())))
    for j in range(c):
        if air[i][j] == -1:
            air_control.append((i, j))
        elif air[i][j] != 0:
            q.append((i, j))
        

# 미세먼지 확산
# 1. bfs를 이용하여 미세먼지가 있는 곳을 queue에 넣고 
# 공기 청정기 작동
# 2. 4방향(우 상 좌 하)를 돌면서 먼지 이동


# 미세먼지 위치
def find_dust(air):
    queue = deque()
    for i in range(r):
        for j in range(c):
            if air[i][j] != 0:
                queue.append((i, j))
    return queue


# 미세먼지 확산
def dust(air):  # air는 미세먼지 분포정보
    
    [print(air[i]) for i in range(len(air))]

    dust_idx = 0
    after_dust = [[0] * c for _ in range(r)] # 먼지가 확산된 후
    dust_cnt = len(q)
    d = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상하좌우
   
    while dust_cnt:
        x, y = q[dust_idx]
        tmp = 0 # x, y 지점 상하좌우 나눠준 것들의 합

        for i in d:
            isControl = False

            nx = x + i[0]
            ny = y + i[1]

            # 공청기 자리인지 확인
            for control in air_control:
                if control[0] == nx and control[1] == ny:
                    isControl = True
                    break
            
            # 정상범위 안에 있다면
            if 0 <= nx < r and 0 <= ny < c and not isControl:
                # 먼지 분포정보 리스트의 x,y 지점의 먼지 // 5
                tmp_dust = air[x][y] // 5
                after_dust[nx][ny] += tmp_dust
                tmp += tmp_dust

                if tmp_dust != 0 and (nx, ny) not in q:
                    q.append((nx, ny))
        after_dust[x][y] += (air[x][y] - tmp)
        dust_cnt -= 1
        dust_idx += 1
    return after_dust



# 공청기 가동
def clean_air(air):
    moving = [(0, 1), (-1, 0), (0, -1), (1, 0)]  # 우상좌하
    idx = 0
    up = [1, 0, 3, 2, 3, 0, 1, 2] # 상우하좌, 하우상좌
    for control in air_control:
        x, y = control
        
        s_x, s_y = x, y
        while True:
            nx, ny = x+moving[up[idx]][0], y+moving[up[idx]][1]

            # 공청기 자리로 오면 idx 옮겨주고 break
            if nx == s_x and ny == s_y:
                idx = (idx+1) % 8
                air[x][y] = 0
                air[nx][ny] = 0
                break
            
            
            air[x][y] = air[nx][ny]
            x = nx
            y = ny 
            

            # 위쪽 끝
            if x == 0 and idx == 0:
                idx = (idx+1) % 8

            # 오른쪽 끝
            elif y == c-1 and (idx ==1 or idx == 5):
                idx = (idx+1) % 8
            
            # 윗부분공기 아래쪽 끝일 때
            elif idx == 2 and x == s_x:
                idx = (idx+1) % 8

            # 아랫쪽 끝
            elif idx == 4 and x == r-1:
                idx = (idx+1) % 8
            
            # 아랫부분공기 위쪽 끝일때
            elif idx == 6 and x == s_x:
                idx = (idx+1) % 8
            



for _ in range(t):
    air = dust(air)
    print("확산")
    [print(air[i]) for i in range(len(air))]

    clean_air(air)
    print("공청기")
    [print(air[i]) for i in range(len(air))]


answer = 0
for i in range(r):
    answer += sum(air[i])

print(answer)