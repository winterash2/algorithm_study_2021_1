INF = int(1e9)

n, m = map(int, input().split())

student_rank = [[INF] * (n + 1) for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    student_rank[a][b] = 1

for i in range(n + 1):
    for j in range(n + 1):
        if i == j:
            student_rank[i][j] = 1

for t in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            student_rank[i][j] = min(student_rank[i][j], student_rank[i][t] + student_rank[t][j])

result = 0
for i in range(1, n + 1):
    count = 0
    for j in range(1, n + 1):
        if student_rank[i][j] < INF or student_rank[j][i] < INF:
            count += 1
    if count == n:
        result += 1

print(result)
