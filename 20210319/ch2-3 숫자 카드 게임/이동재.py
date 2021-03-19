N, M = map(int, input().split())
answer = 0
for _ in range(N):
    answer = max(answer, min(list(map(int, input().split()))))

print(answer)
