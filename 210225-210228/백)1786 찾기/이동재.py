T = list(input())
P = list(input())

KMP = [0 for _ in range(len(P))]

idx = 0
for i in range(1, len(P)):
    while idx > 0 and P[i] != P[idx]:
        idx = KMP[idx-1]
    if P[i] == P[idx]:
        idx += 1
        KMP[i] = idx

for i in range(len(T)):
    


"""
ABC ABCDAB ABCDABCDABDE
ABCDABD
"""
"""
ABCDABDABCDABD
ABCDABD
"""


# 시간 초과....ㅠ
"""
T = list(input())
P = list(input().strip())
pLen = len(P)

dpPrev = []
dpNext = []

answer = []
for i in range(len(T)):
    # print(dpPrev)
    for j in range(len(dpPrev)):
        if T[i] == P[dpPrev[j]]:
            if dpPrev[j] == pLen - 1:
                answer.append(i-pLen+2)
            else:
                dpNext.append(dpPrev[j] + 1)
    if T[i] == P[0]:
        dpNext.append(1)
    dpPrev = dpNext
    dpNext = []

print(len(answer))
print(' '.join(map(str, answer)))
"""
