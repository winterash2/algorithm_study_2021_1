# 80ms 성공
N, K = map(int, input().split())
PH = list(input())
# PH = [0 if x == 'H' else 1 for x in PH]

idxH = 0
idxP = 0
answer = 0
while idxP < N:
    if PH[idxP] == 'P':
        while idxP - idxH > K:
            idxH += 1
        while idxH - idxP <= K:
            if PH[idxH] == 'H':
                PH[idxH] = 'B'
                answer += 1
                break
            idxH += 1
            if idxH >= N:
                break
    if idxH >= N or idxP >= N:
        break
    idxP += 1

print(answer)