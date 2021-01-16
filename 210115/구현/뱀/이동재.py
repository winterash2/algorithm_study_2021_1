# 보드 생성
N = int(input())
board = [[0 for _ in range(N)] for _ in range(N)]
# print(board)

# 사과의 위치를 입력받아 보드에 1로 표시
K = int(input())
for _ in range(K):
    row, col = [int(x) for x in input().split()]
    board[row-1][col-1] = 1  # 사과는 1

L = int(input())
moves = []
for _ in range(L):
    distance, turn = input().split()
    moves.append([int(distance), turn])

# N = 6
# K = 3
# L = 3
# board = [[0, 0, 0, 0, 0, 0],
#          [0, 0, 0, 0, 1, 0],
#          [0, 0, 0, 1, 0, 0],
#          [0, 0, 0, 0, 0, 0],
#          [0, 0, 1, 0, 0, 0],
#          [0, 0, 0, 0, 0, 0]]
# moves = [[3, 'D'], [15, 'L'], [17, 'D']]

# 틀리게 풀었음...난 쓰레기야...
"""
row = col = 0
board[row][col] = 2  # 뱀 몸체는 2
turns = [[0, 1], [1, 0], [0, -1], [-1, 0]]
next_move = 0

apple_count = 0
move_count = 0
is_end = False
for move in moves:
    for _ in range(move[0]-move_count):
        move_count += 1
        row += turns[next_move][0]
        col += turns[next_move][1]
        if row >= N or col >= N or col < 0 or row < 0:  # 벽 부딪히는 조건
            is_end = True
        elif board[row][col] == 2:  # 자기 몸 부딪히는 조건
            is_end = True
        elif board[row][col] == 1:  # 사과를 먹는 조건
            board[row-turns[next_move][0]][col-turns[next_move][1]] = 2
            apple_count += 1
            board[row][col] = 2
            if apple_count == K:
                is_end = True
        else:
            board[row-turns[next_move][0]][col-turns[next_move][1]] = 0
            board[row][col] = 2
        if is_end:
            break
    if is_end:
        break
    if move[1] == 'D':
        next_move += 1
        if next_move == 4:
            next_move = 0
    elif move[1] == 'L':
        next_move -= 0
        if next_move == -1:
            next_move = 3

print(move_count)
"""
# 근데 입력예시2는 4 나오는게 정상 아님?
