## 뇌가 죽은거같아오............실패...다시해보껭....

n,m=map(int,input().split())
user_info=list(map(int,input().split()))

# 현재 위치
user_pos=user_info[0:2]
# 보고있는곳
user_eye=user_info[2]

# 북동남서
eye=[0,1,2,3]
#이동
mov=[-1,1,1,-1]

# 바다=1 육지=0
land=[
    [1,1,1,1],
    [1,0,0,1],
    [1,1,0,1],
    [1,1,1,1]
    ]

def left(now_eye):
    if now_eye==3:
        now_eye=0
    else:
        now_eye+=1
    return now_eye

count=0
left_eye=left(user_eye)
num=0
while True:
    print(user_pos, num,  land[user_pos[0]][user_pos[1]])

    # 영역표시o
    land[user_pos[0]][user_pos[1]]=1

    # 한바퀴 돌면 끝 o
    if num==4:
        break
    
    # 북 or 남 => x가 움직여야해용
    if left_eye==0 or 2:
        x_pos=user_pos[0]+mov[left_eye]
        print(x_pos)
        if land[x_pos][user_pos[1]]==1 or x_pos>(n-1) or x_pos<0:
            left_eye=left(left_eye)
            num+=1
        else:
            user_pos[0]+=1
            num=0

    #동 or 서 => y가 움직여야해용
    else:
        y_pos=user_pos[1]+mov[left_eye]
        print(y_pos)
        if land[user_pos[0]][y_pos]==1 or y_pos>(m-1) or y_pos<0:
            left_eye=left(left_eye)
            num+=1
        else:
            user_pos[1]+=1
            num=0
    count+=1
    
print(land)
print(count)