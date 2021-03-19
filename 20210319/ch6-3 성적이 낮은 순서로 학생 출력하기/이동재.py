N = int(input())
scores = []
for _ in range(N):
    name, score = input().split()
    score = int(score)
    scores.append((name, score))
scores.sort(key=lambda x: x[1])
for name, socre in scores:
    print(name, end=' ')