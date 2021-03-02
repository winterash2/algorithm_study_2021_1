from collections import deque

M, N = map(int, input().split())  # i가 N, j가 M임
farm = []
q = deque()
for _ in range(N):
    farm.append(list(map(int, input().split())))

for i in range(N):
    for j in range(M):
        if farm[i][j] == 1:
            q.append((i, j))

answer = -1
while q:
    answer += 1
    for _ in range(len(q)):
        n, m = q.popleft()
        # print(n, m)
        if n+1 < N and farm[n+1][m] == 0:
            farm[n+1][m] = 1
            q.append((n+1, m))
        if n-1 >= 0 and farm[n-1][m] == 0:
            farm[n-1][m] = 1
            q.append((n-1, m))
        if m+1 < M and farm[n][m+1] == 0:
            farm[n][m+1] = 1
            q.append((n, m+1))
        if m-1 >= 0 and farm[n][m-1] == 0:
            farm[n][m-1] = 1
            q.append((n, m-1))
    # print("-"*50, answer)
    # [print(x) for x in farm]

enable = True
for i in range(N):
    for j in range(M):
        if farm[i][j] == 0:
            enable = False
            break
    if not enable:
        break

if enable:
    print(answer)
else:
    print(-1)
