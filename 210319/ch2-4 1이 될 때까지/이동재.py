N, K = map(int, input().split())
answer = 0
while N > 1:
    diff = N % K
    if diff == 0:
        answer += 1
        N /= K
    else:
        answer += int(diff)
        N -= diff

print(answer)