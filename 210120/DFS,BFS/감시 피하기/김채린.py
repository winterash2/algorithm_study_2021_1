from itertools import combinations

n = int(input()) 
board = [] 
teachers = [] 
spaces = [] 

for i in range(n):
    board.append(list(input().split()))

    for j in range(n):

        # 선생님이 존재하는 위치 
        if board[i][j] == 'T':
            teachers.append((i, j))

        # 장애물을 설치 위치
        if board[i][j] == 'X':
            spaces.append((i, j))

def watch(x, y, direction):

    # 왼쪽
    if direction == 0:

        while y >= 0:
            if board[x][y] == 'S': # 학생
                return True

            if board[x][y] == 'O': # 장애물
                return False
            y -= 1

    # 오른쪽
    if direction == 1:
        while y < n:
            if board[x][y] == 'S': 
                return True

            if board[x][y] == 'O': 
                return False
            y += 1

    # 위
    if direction == 2:

        while x >= 0:
            if board[x][y] == 'S':
                return True

            if board[x][y] == 'O':
                return False
            x -= 1

    # 아래
    if direction == 3:

        while x < n:
            if board[x][y] == 'S':
                return True

            if board[x][y] == 'O':
                return False
            x += 1
    return False


def process():
    # 모든 선생의 위치 확인
    for x, y in teachers:
        for i in range(4):
            if watch(x, y, i):
                return True
    return False

find = False 

for data in combinations(spaces, 3):
    # 장애물설치
    for x, y in data:
        board[x][y] = 'O'
    
    if not process():
        find = True
        break
    
    for x, y in data:
        board[x][y] = 'X'

if find:
    print('YES')
else:
    print('NO')