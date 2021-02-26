# http://boj.kr/18808
import copy

# 스티커가 노트북에 붙는지 확인
# 붙일 수 있으면 laptop에 스티커 값 설정 후 True 리턴, 못 붙이면 False
def check(x, y):
    for i in range(c):
        for j in range(r):
            if sticker[i][j] ==1 and laptop[x+i][y+j] == 1:
                return False

    for i in range(c):
        for j in range(r):
            if sticker[i][j] == 1:
                laptop[x+i][y+j] = 1
    return True



# 회전이 필요하면 수행(파라미터로 들어온 rotate가 1일 때) 후 check함수 호출로 스티커를 붙일 수 있는지 확인
def stick_to_laptop(rotate):
    global sticker, r, c
    if rotate:
        result = []
        for l in zip(*sticker):
            print(">", l)
            result.append(list(reversed(l)))
        sticker = copy.deepcopy(result)
        c, r = len(sticker), len(sticker[0])  # 회전됐으므로 r, c 값 재설정

    # 스티커가 노트북 안에서 움직일 수 있는 범위 안에서 check함수 호출
    for i in range(0, l_c-c+1):
        for j in range(0, l_r-r+1):
            if check(i, j):
                return 1

    return 0




# 노트북 크기
l_c, l_r, t = map(int, input().split())
laptop = [[0] * l_r for _ in range(l_c)]

for _ in range(t):
    # 스티커 크기
    c, r = map(int, input().split())
    sticker = [] * r
    for i in range(c):
        sticker.append(list(map(int, input().split())))

    
    possible = stick_to_laptop(0)
    for _ in range(3): # 들어온대로 못 붙이고 회전이 필요한 경우
        if possible == 0:
            possible = stick_to_laptop(1)


# 정답 출력
answer = 0
for i in range(l_c):
    for j in range(l_r):
        if laptop[i][j] == 1:
            answer += 1
print(answer)