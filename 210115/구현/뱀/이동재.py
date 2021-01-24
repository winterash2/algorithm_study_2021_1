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
moves.append((-1, 'L')) # 끝까지 다 돌고 나서 더 이상 안 돌 때 확인용
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

directions = [[-1,0], [0,-1],[1,0],[0,1]] # 상 좌 하 우

x, y = 0, 0
direction = 3
def turn(C):
    global direction
    if C == 'L':
        direction = 0 if direction == 3 else direction + 1
    else:
        direction = 3 if direction == 0 else direction - 1

snake = [(0,0)]
second = 0
next_move = moves[0]
moves = moves[1:]

while True:
    second += 1
    nx = x + directions[direction][0]
    ny = y + directions[direction][1]
    # print("nx=",nx,"ny=", ny)
    if nx < 0 or nx >= N or ny < 0 or ny >= N: # 맵을 벗어나면 끝
        break
    if (nx,ny) in snake: # 자기 몸통에 부딪히면 끝
        break
    # 다음 칸에 정상적으로 갈 수 있는 경우
    snake.append((nx,ny))
    if board[nx][ny] == 0: # 사과가 아닐 때는 자기 몸 구성하는 것 중 가장 먼저 들어온것을 제거
        snake = snake[1:]
    else: # 사과일 경우 사과를 먹었으니까 없애줌
        board[nx][ny] = 0
    if second == next_move[0]:
        turn(next_move[1])
        next_move = moves[0]
        moves = moves[1:]
    x, y = nx, ny

print(second)










    # 1차 시도
    # 배열에 뱀 몸통 걍 2로 표시했는데 이렇게하면 맨 뒤에 있는거 못 빼는데 왜 이렇게 한거야...
    # 난 쓰레기야...
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
