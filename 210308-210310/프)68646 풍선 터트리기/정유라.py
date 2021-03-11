# https://programmers.co.kr/learn/courses/30/lessons/68646

def solution(a):
    left_small = [0] * len(a)
    right_small = [0] * len(a)
    
    # 각 구간 최소값 넣기
    l_min_value = int(1e9)
    for i in range(len(a)):
        # print(a[i], a[-i-1])
        if l_min_value > a[i]:
            left_small[i] = a[i]
            l_min_value = a[i]
        else:
            left_small[i] = left_small[i-1]
            
    r_min_value = int(1e9)
    for i in range(len(a)-1, -1, -1):
        if r_min_value > a[i]:
            right_small[i] = a[i]
            r_min_value = a[i]
        else:
            right_small[i] = right_small[i+1]

    answer = 2   # 양 옆 끝 원소는 무조건 포함된다
    for i in range(1, len(a)-1):
        if max(left_small[i-1], a[i], right_small[i+1]) == a[i]:
            continue
        answer += 1  
    
    return answer

solution([-16,27,65,-2,58,-92,-71,-68,-61,-33])
# solution([9,-1,-5])