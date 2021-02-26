# http://boj.kr/3678
# 어디서 인덱스에러가 나는거징..

# 1. 기본 4방향, 보조 2방향
#    우상향, 좌상향, 좌하향, 우하향, 상, 하
#       0      1       2       3     4   5


# 자원 할당
def assign_resource(MAP, i, resource_idx):
    global x, y
    nx = x + dx[i]
    ny = y + dy[i]
    if 0 <= nx < c and 0 <= ny < r:
        if MAP[ny][nx] == 0:
            value = best_value(nx, ny)
            MAP[ny][nx] = value
            answer[resource_idx] = value
            resource_cnt[value] += 1
            x, y = nx, ny
        else:
            if i == 0: # 우상향 -> 우하향
                assign_resource(MAP, 3, resource_idx)
            elif i == 1: # 좌상향 -> 상향
                assign_resource(MAP, 4, resource_idx)
            elif i == 3: # 우하향 -> 하향
                assign_resource(MAP, 5, resource_idx)
            elif i == 4: # 상향 -> 우상향
                assign_resource(MAP, 0, resource_idx)
            elif i == 2: # 좌하향 -> 좌상향
                assign_resource(MAP, 1, resource_idx)
            elif i == 5: # 하향 -> 좌하향
                assign_resource(MAP, 2, resource_idx)
            return False
    return True

# 할당할 값 구하기
def best_value(x, y):
    tmp_resources = list(range(1, 6))
    for i in range(6):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < c and 0 <= ny < r:
            if MAP[ny][nx] in tmp_resources:
                tmp_resources.remove(MAP[ny][nx])
        
    min_val = 1e9
    min_val_idx = 0
    # 선정된 자원들 중에서 cnt가 가장 적은 값
    for resource in tmp_resources:
        if min_val > resource_cnt[resource]:
            min_val = resource_cnt[resource]
            min_val_idx = resource

    return min_val_idx
    


dx = [-1, -1, 1, 1, -2, 2] # 배열에 육각형을 구현하는 것이므로 위로 한칸은 실질적으로 두칸 올려야함
dy = [1, -1, -1, 1, 0, 0]
n = 1000
r = c = 5000

# 맵 초기화
MAP = [[0]*c for _ in range(r)]
x, y = c//2, r//2
MAP[y][x] = 1
resource_idx = 2

# 몇번째 칸에 어떤 자원값이 들어있는지 (정답배열)
answer = [0] * (n+1)
answer[1] = 1

# 자원 카운트
resource_cnt = [0] * (6)
resource_cnt[0] = 1e9
resource_cnt[MAP[y][x]] += 1 # 첫 번째 칸 1로 초기화
idx = 0 # 방향을 위한 인덱스

while resource_idx != n + 1:
    res = assign_resource(MAP, idx, resource_idx)
    if res: # 제대로 값이 할당되었으면
        idx = (idx+1) % 4 # 방향 전환
    else: 
        pass
    resource_idx += 1


for _ in range(int(input())):
    t = int(input())
    print(answer[t])