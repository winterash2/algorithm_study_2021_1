import sys
# import copy
input = sys.stdin.readline

def checking(temp, sticker):
    for sy in range(len(sticker)):
        for sx in range(len(sticker[0])):
            if temp[i+sy][j+sx] + sticker[sy][sx] > 1:
                return False
    return True

def attach(temp, sticker):
    for sy in range(len(sticker)):
        for sx in range(len(sticker[0])):
            temp[i+sy][j+sx] += sticker[sy][sx]
    return

def rotate_90(arr):
    n = len(arr)
    m = len(arr[0])

    result = [[0]*n for _ in range(m)]

    for i in range(n):
        for j in range(m):
            result[j][n-i-1] = arr[i][j]
    return result


Y, X, k = map(int, input().split())
notebook = [[0] * X for _ in range(Y)]

for _ in range(k):
    y, x = map(int, input().split())
    sticker = [list(map(int, input().split())) for _ in range(y)]
    chk = False
    cnt = 0
    # for i in range(4):
    while cnt < 4:
        if chk == True:
            break
        for i in range(Y - len(sticker) + 1):
            if chk == True:
                break
            for j in range(X - len(sticker[0]) + 1):
                # temp = copy.deepcopy(notebook)
                if checking(notebook, sticker):
                    # notebook = temp
                    attach(notebook, sticker)
                    chk = True
                    break
        sticker = rotate_90(sticker)
        cnt += 1

answer = 0
for i in range(Y):
    for j in range(X):
        answer += notebook[i][j]

print(answer)