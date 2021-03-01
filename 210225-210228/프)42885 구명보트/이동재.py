# 테스트 1 〉	통과 (1.27ms, 10.2MB)
# 테스트 2 〉	통과 (1.08ms, 10.1MB)
# 테스트 3 〉	통과 (1.02ms, 10.2MB)
# 테스트 4 〉	통과 (0.88ms, 10.2MB)
# 테스트 5 〉	통과 (0.52ms, 10.2MB)
# 테스트 6 〉	통과 (0.37ms, 10.2MB)
# 테스트 7 〉	통과 (0.51ms, 10.1MB)
# 테스트 8 〉	통과 (0.04ms, 10.2MB)
# 테스트 9 〉	통과 (0.08ms, 10.2MB)
# 테스트 10 〉	통과 (1.04ms, 10.3MB)
# 테스트 11 〉	통과 (0.90ms, 10.2MB)
# 테스트 12 〉	통과 (0.79ms, 10.2MB)
# 테스트 13 〉	통과 (0.97ms, 10.3MB)
# 테스트 14 〉	통과 (1.28ms, 10.2MB)
# 테스트 15 〉	통과 (0.10ms, 10.2MB)
# 효율성  테스트
# 테스트 1 〉	통과 (9.30ms, 10.6MB)
# 테스트 2 〉	통과 (10.52ms, 10.5MB)
# 테스트 3 〉	통과 (10.02ms, 10.5MB)
# 테스트 4 〉	통과 (10.20ms, 10.5MB)
# 테스트 5 〉	통과 (9.88ms, 10.4MB)
def solution(people, limit):
    answer = 0
    people.sort()
    idxMin = 0
    idxMax = len(people) - 1
    while idxMax >= idxMin:
        answer += 1
        if people[idxMax] + people[idxMin] <= limit:
            idxMin += 1
        idxMax -= 1
    return answer


# 무거운 놈들을 먼저 빼면 되겠지 싶어서 해본 것
# 실패함 합계: 60.0 / 100.0
# 구명보트에 2명만 탈 수 있다는 조건을 못 보고 한 것
"""
def solution(people, limit):
    answer = 0
    people.sort(reverse=True)

    while people:
        answer += 1
        cur = []
        curWeight = 0
        for i in range(len(people)):
            if people[i] + curWeight <= limit:
                cur.append(people[i])
                curWeight += people[i]  
        for elem in cur:
            people.remove(elem)
        
    return answer
"""

print(solution([70, 50, 80, 50], 100))
print(solution([70, 80, 50], 100))
