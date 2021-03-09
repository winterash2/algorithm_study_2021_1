def solution(m, n, puddles):
    graph = [[True for _ in range(m+1)] for _ in range(n+1)] # True는 막히지 않은 길
    for p in puddles:
        graph[p[1]][p[0]] = False # False는 막힌 길, 즉 웅덩이
    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
    dp[0][1] = 1
    
    for i in range(1, n+1):
        for j in range(1, m+1):
            if graph[i][j]:
                dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % 1000000007

    answer = dp[n][m]
    return answer

m, n = 4, 3
puddles = [[2, 2]]
print(solution(m, n, puddles))
# 정확성  테스트
# 테스트 1 〉	통과 (0.02ms, 10.2MB)
# 테스트 2 〉	통과 (0.02ms, 10.2MB)
# 테스트 3 〉	통과 (0.04ms, 10.3MB)
# 테스트 4 〉	통과 (0.05ms, 10.2MB)
# 테스트 5 〉	통과 (0.09ms, 10.1MB)
# 테스트 6 〉	통과 (0.07ms, 10.2MB)
# 테스트 7 〉	통과 (0.07ms, 10.3MB)
# 테스트 8 〉	통과 (0.15ms, 10.2MB)
# 테스트 9 〉	통과 (0.07ms, 10.2MB)
# 테스트 10 〉	통과 (0.05ms, 10.3MB)
# 효율성  테스트
# 테스트 1 〉	통과 (2.85ms, 10.4MB)
# 테스트 2 〉	통과 (1.38ms, 10.2MB)
# 테스트 3 〉	통과 (1.67ms, 10.3MB)
# 테스트 4 〉	통과 (2.23ms, 10.4MB)
# 테스트 5 〉	통과 (1.38ms, 10.2MB)
# 테스트 6 〉	통과 (2.91ms, 10.3MB)
# 테스트 7 〉	통과 (1.60ms, 10.2MB)
# 테스트 8 〉	통과 (2.27ms, 10.2MB)
# 테스트 9 〉	통과 (2.39ms, 10.2MB)
# 테스트 10 〉	통과 (2.27ms, 10.3MB)
# 채점 결과
# 정확성: 50.0
# 효율성: 50.0
# 합계: 100.0 / 100.0