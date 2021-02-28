# 시간 초과....ㅠ
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
ABC ABCDAB ABCDABCDABDE
ABCDABD
"""
"""
ABCDABDABCDABD
ABCDABD
"""