# 원래 내가 풀었던 것
# 책 코드보다 구현은 조금 어려운데 시간은 훨씬 빠름
# 테스트 1 〉	통과 (0.02ms, 10.2MB)
# 테스트 2 〉	통과 (0.09ms, 10.1MB)
# 테스트 3 〉	통과 (1.30ms, 10.6MB)
# 테스트 4 〉	통과 (5.68ms, 10.9MB)
# 테스트 5 〉	통과 (12.63ms, 15MB)
# 테스트 6 〉	통과 (0.17ms, 10.1MB)
# 테스트 7 〉	통과 (0.91ms, 10.3MB)
# 테스트 8 〉	통과 (6.07ms, 10.9MB)
# 테스트 9 〉	통과 (13.18ms, 15.1MB)
# 테스트 10 〉	통과 (6.48ms, 10.8MB)
# 테스트 11 〉	통과 (6.19ms, 10.9MB)
# 테스트 12 〉	통과 (9.35ms, 11.4MB)
# 테스트 13 〉	통과 (10.39ms, 11.5MB)
# 테스트 14 〉	통과 (0.03ms, 10.3MB)
# 테스트 15 〉	통과 (4.51ms, 10.6MB)
# 테스트 16 〉	통과 (2.52ms, 10.2MB)
# 테스트 17 〉	통과 (4.26ms, 10.6MB)
# 테스트 18 〉	통과 (2.23ms, 10.3MB)
# 테스트 19 〉	통과 (0.81ms, 10.2MB)
# 테스트 20 〉	통과 (3.08ms, 10.4MB)
# 테스트 21 〉	통과 (6.52ms, 10.9MB)
# 테스트 22 〉	통과 (13.37ms, 18.3MB)
# 테스트 23 〉	통과 (13.30ms, 11.7MB)
# 테스트 24 〉	통과 (11.98ms, 11.6MB)
# 테스트 25 〉	통과 (0.01ms, 10.2MB)
# 테스트 26 〉	통과 (0.01ms, 10.2MB)
# 테스트 27 〉	통과 (0.01ms, 10.2MB)
def solution(N, stages):
    answer = []
    positions = [0]*(N+2)

    for i in stages:
        positions[i] += 1

    success = 0
    fail_rates = []
    for i in range(N, 0, -1):
        success += positions[i+1]
        if success == 0 and positions[i] == 0:
            fail_rates.append((0, i))
        else:
            fail_rates.append((positions[i] / (success+positions[i]), i))
        
    fail_rates.sort(key=lambda x: (-x[0], x[1]))

    for fail in fail_rates:
        answer.append(fail[1])

    return answer

# 책 정답 참고해서 짠 코드
# 코딩은 더 쉬우나 시간은 훨씬 많이 걸림
# 시간은 동빈코드랑 유사하게 나옴
# 테스트 1 〉	통과 (0.02ms, 10.1MB)
# 테스트 2 〉	통과 (0.20ms, 10.2MB)
# 테스트 3 〉	통과 (69.06ms, 10.4MB)
# 테스트 4 〉	통과 (325.43ms, 10.8MB)
# 테스트 5 〉	통과 (1390.32ms, 15MB)
# 테스트 6 〉	통과 (2.51ms, 10.2MB)
# 테스트 7 〉	통과 (12.79ms, 10.3MB)
# 테스트 8 〉	통과 (344.53ms, 10.9MB)
# 테스트 9 〉	통과 (1386.50ms, 15MB)
# 테스트 10 〉	통과 (137.97ms, 10.9MB)
# 테스트 11 〉	통과 (350.27ms, 10.9MB)
# 테스트 12 〉	통과 (200.24ms, 11.5MB)
# 테스트 13 〉	통과 (449.63ms, 11.3MB)
# 테스트 14 〉	통과 (0.06ms, 10.2MB)
# 테스트 15 〉	통과 (10.55ms, 10.6MB)
# 테스트 16 〉	통과 (5.58ms, 10.4MB)
# 테스트 17 〉	통과 (12.12ms, 10.5MB)
# 테스트 18 〉	통과 (5.48ms, 10.3MB)
# 테스트 19 〉	통과 (1.48ms, 10.3MB)
# 테스트 20 〉	통과 (9.85ms, 10.4MB)
# 테스트 21 〉	통과 (16.01ms, 10.8MB)
# 테스트 22 〉	통과 (1116.24ms, 18.3MB)
# 테스트 23 〉	통과 (14.19ms, 11.5MB)
# 테스트 24 〉	통과 (58.89ms, 11.6MB)
# 테스트 25 〉	통과 (0.01ms, 10.2MB)
# 테스트 26 〉	통과 (0.01ms, 10.3MB)
# 테스트 27 〉	통과 (0.01ms, 10.1MB)
def solution(N, stages):
    answer = []

    dodal = len(stages)
    fail_rates = []
    for i in range(1, N+1):
        not_clear = stages.count(i)
        
        if dodal == 0:
            fail_rates.append((0, i))
            continue
        else:
            fail_rates.append((not_clear / dodal, i))
            dodal -= not_clear
    fail_rates.sort(key = lambda x : (-x[0], x[1]))

    for f in fail_rates:
        answer.append(f[1])

    return answer

N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]
result = [3, 4, 2, 1, 5]

print(result)
print(solution(N, stages))
