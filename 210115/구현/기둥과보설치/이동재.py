# 체크
def check(answer):
    for frame in answer:
        validation = False
        x, y, a = frame
        if a == 0:  # 기둥
            if y == 0:  # 바닥에 닿아있으면
                validation = True
            elif [x-1, y, 1] in answer:  # 설치 지점 왼쪽에 오른쪽으로 뻗어나오는 보가 있으면
                validation = True
            elif [x, y, 1] in answer:# !!!이 조건은 생각을 못 했었음!!!! 설치 지점부터 오른쪽으로 뻗어나가는 보가 있으면
                validation = True
            elif [x, y-1, 0] in answer:  # 설치 지점 아래에 기둥이 세워져있으면
                validation = True
        else:  # 보
            if y == 0:  # 바닥에 보를 설치하려고 하면 종료
                return answer
            elif [x, y-1, 0] in answer:  # 설치하려고 하는 보의 왼쪽 아래에 기둥이 있으면
                validation = True
            elif [x+1, y-1, 0] in answer:  # 설치하려고 하는 보의 오른쪽 아래에 기둥이 있으면
                validation = True
            elif [x-1, y, 1] in answer:  # 설치하려고 하는 보의 좌우에 보가 있으면
                if [x+1, y, 1] in answer:
                    validation = True
        if not validation:  # validation이 False면, 즉, 적합하지 않은게 하나라도 나오면 중단하고 False를 리턴
            return False
    return True


def solution(n, build_frame):
    answer = []

    for frame in build_frame:
        x, y, a, b = frame
        frame = [x, y, a]
        if b == 0:  # 삭제
            if frame in answer:
                answer.remove(frame)
                if not check(answer):
                    answer.append(frame)
        else:  # 설치
            if frame not in answer:
                answer.append(frame)
                if not check(answer):
                    answer.remove(frame)

    answer.sort()
    return answer


n = 5
build_frame = [[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [
    2, 2, 1, 1], [5, 0, 0, 1], [5, 1, 0, 1], [4, 2, 1, 1], [3, 2, 1, 1]]
result = [[1, 0, 0], [1, 1, 1], [2, 1, 0], [2, 2, 1],
          [3, 2, 1], [4, 2, 1], [5, 0, 0], [5, 1, 0]]
build_frame = [[0, 0, 0, 1], [2, 0, 0, 1], [4, 0, 0, 1], [0, 1, 1, 1], [
    1, 1, 1, 1], [2, 1, 1, 1], [3, 1, 1, 1], [2, 0, 0, 0], [1, 1, 1, 0], [2, 2, 0, 1]]
result = [[0,0,0],[0,1,1],[1,1,1],[2,1,1],[3,1,1],[4,0,0]]
print("True" if solution(n, build_frame) == result else "False")
