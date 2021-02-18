# https://programmers.co.kr/learn/courses/30/lessons/42860

# a랑 z중에 더 가까운 것과의 차이
# A B C  D E F G H I J  K L  M   N O   P Q   R  S T  U  V  w  X  y  Z 
# 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26

name = list(input())
print(name)


# 26 - index > index 
# A: 65

# 해당 알파벳을 만들기 위해 조작해야하는 횟수로 저장
convert_alpha = []
for i in name:
    alpha_value = ord(i)-65
    if 26 - alpha_value >= alpha_value:
        convert_alpha.append(alpha_value)
    else:
        convert_alpha.append(26-alpha_value)

print("conver:", convert_alpha)

# 근처에 A가 많을 수록 A가 가는 방향으로 가면(이미 맞춰진 알파벳인 경우도) 이동거리가 더 나오기때문

# 오른쪽으로 가면서 A가 아닌 알파벳 자리 찾기
def find_right_not_zero(idx, convert_alpha):
    cnt = 1
    idx += 1
    

    while True:
        if idx >= len(convert_alpha): # 배열 끝에서 오른쪽으로 갔을 때
            idx -= len(convert_alpha)
            
        if convert_alpha[idx] != 0:
            return idx, cnt
        cnt += 1
        idx += 1

# 왼쪽으로 가면서 A가 아닌 알파벳 자리 찾기
def find_left_not_zero(idx, convert_alpha):
    cnt = 1
    idx -= 1
    while True:
        if idx < 0: # 배열 맨 앞에서 왼쪽
            idx += len(convert_alpha)
        if convert_alpha[idx] != 0:
            return idx, cnt
        
        cnt += 1
        idx -= 1


idx = 0     # 현재 자리
total = 0   # 총 조작 횟수
while True:
    # 알파벳 만들기
    total += convert_alpha[idx]
    convert_alpha[idx] = 0 # 만들고 나면 0으로 바꿔주기
    print("-------total:", total, "idx:", idx)

    # 모두 0인지 확인
    if convert_alpha.count(0) == len(convert_alpha):
        print(total)
        break

    # 오른쪽, 왼쪽으로 찾으면서 0이 아닌 알파벳 찾기
    current_ridx, r_not_zero_cnt = find_right_not_zero(idx, convert_alpha)
    current_lidx, l_not_zero_cnt = find_left_not_zero(idx, convert_alpha)
    
  
    if l_not_zero_cnt < r_not_zero_cnt:
        print("l<r 왼쪽으로 이동")
        idx = current_lidx
        total += l_not_zero_cnt
    else:
        print("r<=l 오른쪽으로 이동")
        idx = current_ridx
        total += r_not_zero_cnt