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