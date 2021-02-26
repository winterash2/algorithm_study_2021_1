N, M = map(int, input().split())
board = [[] for _ in range(N)]
for i in range(N):
    board[i] = [0 if c == 'W' else 1 for c in input()]

# [print(board[i]) for i in range(len(board))]

answer = 1e9
for baseY in range(N-8+1):
    for baseX in range(M-8+1):
        count = 0
        for i in range(8):
            for j in range(8):
                if board[baseY+i][baseX+j] != (i+j)%2:
                    count += 1
        count = min(count, 64 - count)
        answer = min(answer, count)

print(answer)