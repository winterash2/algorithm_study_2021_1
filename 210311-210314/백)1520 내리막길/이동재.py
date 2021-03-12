import sys
input = sys.stdin.readline

M, N = map(int, input().split())
table = []
for _ in range(M):
    table.append(list(map(int, input().split())))
blocks = []
for x in range(N):
    for y in range(M):
        blocks.append((table[y][x], x, y))
blocks.sort()

def calc(table, x, y):
    q = [(x, y)]
    answer = 0
    while q:
        x, y = q.pop()
        # print(x, y)
        if x == N-1 and y == M-1:
            answer += 1
            continue
        for d in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx = x + d[0]
            ny = y + d[1]
            if 0 <= nx < N and 0 <= ny < M:
                if table[ny][nx] < table[y][x]:
                    q.append((nx, ny))
    return answer

dp = [[0 for _ in range(N)] for _ in range(M)]

for block in blocks:
    val, x, y = block
    if x == N-1 and y == M-1:
        dp[y][x] = 1
    else:
        temp = 0
        for d in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx = x + d[0]
            ny = y + d[1]
            if 0 <= nx < N and 0 <= ny < M:
                if table[ny][nx] < table[y][x]:
                    temp += dp[ny][nx]
        dp[y][x] = temp
        if x == 0 and y == 0:
            break

print(dp[0][0])

# 1차, 그냥 깡으로 다 하는거 - 실패
"""
M, N = map(int, input().split())
table = []
for _ in range(M):
    table.append(list(map(int, input().split())))

q = [(0,0)]
answer = 0
while q:
    x, y = q.pop()
    # print(x, y)
    if x == N-1 and y == M-1:
        answer += 1
        continue
    for d in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx = x + d[0]
        ny = y + d[1]
        if 0 <= nx < N and 0 <= ny < M:
            if table[ny][nx] < table[y][x]:
                q.append((nx, ny))

print(answer)
"""