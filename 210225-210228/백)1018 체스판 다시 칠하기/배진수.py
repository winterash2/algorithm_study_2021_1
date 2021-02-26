import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = []
for i in range(n):
    board.append(input().rstrip())

temp_W = ['WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW']
temp_B = ['BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB']


def check(board, y, x):
    cntW = 0
    cntB = 0
    for i in range(8):
        for j in range(8):
            if board[y + i][x + j] != temp_W[i][j]:
                cntW += 1
        
            if board[y + i][x + j] != temp_B[i][j]:
                cntB += 1

    return min(cntW, cntB)


answer = int(1e9)
for i in range(n - 8 + 1):
    for j in range(m - 8 + 1):
        answer = min(answer, check(board, i, j))

print(answer)
