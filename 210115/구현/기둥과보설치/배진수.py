def check(answer):
    for x, y, a in answer:
        if a == 0:
            if y == 0 or [x-1,y,1] in answer or [x,y,1] in answer or [x,y-1,0] in answer:
                continue
            else:
                return False
        elif a == 1:
            if [x,y-1,0] in answer or [x+1,y-1,0] in answer or ([x-1,y,1] in answer and [x+1,y,1] in answer):
                continue
            else:
                return False
    return True

def solution(n, build_frame):
    len_build = len(build_frame)
    answer = []
    
    for frame in build_frame:
        x, y, a, b = frame
        if b == 1:
            answer.append([x,y,a])
            if check(answer) is not True:
                answer.remove([x,y,a])
        elif b == 0:
            answer.remove([x,y,a])
            if check(answer) is not True:
                answer.append([x,y,a])
    answer = sorted(answer)
    return answer


n = 5
build_frame = [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]
print(solution(n, build_frame))