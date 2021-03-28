# https://programmers.co.kr/learn/courses/30/lessons/42895

# 1. dfs 이용 다해보는 경우
# 2. 종료조건 
#   1) number를 만들수있는 경우 N을 사용한 횟수 갱신 후 종료
#   2) 횟수가 8보다 크면 종료

answer = -1
def dfs(N, number, result, count):
    global answer
    # 종료 조건
    if number == result:
        if answer == -1:
            answer = count
        else:
            answer = min(answer, count)
    
    if count > 8:
        return

    nn = 0
    for i in range(1, 8-count):
        nn = nn * 10 + N

        dfs(N, number, result+nn, count+i)
        dfs(N, number, result-nn, count+i)
        dfs(N, number, result*nn, count+i)
        dfs(N, number, result/nn, count+i)


def solution(N, number):
    dfs(N, number, 0, 0)
    return answer


print(solution(5, 12)) # 4
print(solution(2, 11)) # 3