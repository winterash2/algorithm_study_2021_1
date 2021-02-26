# https://programmers.co.kr/learn/courses/30/lessons/42885

# 1. people 정렬
# 2. 몸무게가 제일큰 + 제일작 < 100 이면 answer+1, 둘다 빼기
# 2-1. > 100 이면 제일큰 만 빼기
# 덱에 한 개만 남아있는 경우 answer +1 후 종료

from collections import deque
def solution(people, limit):
    answer = 0
    
    people.sort()
    q = deque(people)
    
    while q:
        if len(q) == 1:
            answer += 1
            break
        big, small = q[0], q.pop()
        if small + big <= limit:
            q.popleft()
        answer += 1

    return answer