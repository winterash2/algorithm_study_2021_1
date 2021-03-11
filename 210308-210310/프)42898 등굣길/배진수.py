
def solution(m, n, puddles):
    dp = [[0] * m for _ in range(n)]

    for pudd in puddles:
        x, y = pudd
        dp[y-1][x-1] = -1

    for i in range(n):
        if dp[i][0] == -1:
            break
        dp[i][0] = 1
    for j in range(m):
        if dp[0][j] == -1:
            break
        dp[0][j] = 1

    for i in range(1, n):
        for j in range(1, m):
            if dp[i][j] == -1:
                continue
            else:
                if dp[i-1][j] == -1:
                    dp[i][j] = dp[i][j-1]
                elif dp[i][j-1] == -1:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
    return dp[-1][-1]
"""
이게 말이됩니까~~ 효율적이게 다 통과하는데 왜 효율성 테스트 실패야

정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.3MB)
테스트 2 〉	통과 (0.02ms, 10.4MB)
테스트 3 〉	통과 (0.03ms, 10.2MB)
테스트 4 〉	통과 (0.04ms, 10.3MB)
테스트 5 〉	통과 (0.08ms, 10.3MB)
테스트 6 〉	통과 (0.05ms, 10.3MB)
테스트 7 〉	통과 (0.05ms, 10.2MB)
테스트 8 〉	통과 (0.13ms, 10.3MB)
테스트 9 〉	통과 (0.07ms, 10.3MB)
테스트 10 〉	통과 (0.03ms, 10.2MB)
효율성  테스트
테스트 1 〉	실패 (3.10ms, 10.4MB)
테스트 2 〉	실패 (1.55ms, 10.3MB)
테스트 3 〉	실패 (1.68ms, 10.3MB)
테스트 4 〉	실패 (2.40ms, 10MB)
테스트 5 〉	실패 (1.99ms, 10.2MB)
테스트 6 〉	실패 (3.19ms, 10.4MB)
테스트 7 〉	실패 (1.59ms, 10.2MB)
테스트 8 〉	실패 (2.46ms, 10.3MB)
테스트 9 〉	실패 (2.56ms, 10.3MB)
테스트 10 〉	실패 (2.58ms, 10.2MB)
"""

m = 4
n = 3
puddles = [[2, 2]]
print(solution(m, n, puddles))

# dfs로 풀면 당근 효율성 실패(시간초과)
# mx = [1, 0]
# my = [0, 1]


# def solution(m, n, puddles):
#     answer = []
#     arr = [[0] * m for _ in range(n)]
#     for pudd in puddles:
#         x, y = pudd
#         arr[y-1][x-1] = 1

#     def dfs(x, y):
#         print(x, y)
#         if x == (n-1) and y == (m-1):
#             answer.append(1)
#         else:
#             for i in range(2):
#                 dx = x + mx[i]
#                 dy = y + my[i]
#                 if 0 <= dx < n and 0 <= dy < m:
#                     if arr[dx][dy] == 1:
#                         continue
#                     else:
#                         dfs(dx, dy)
#     dfs(0, 0)

#     return len(answer)