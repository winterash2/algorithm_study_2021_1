from collections import deque

# 1차 시도
# 제대로 동작하지 않음
# 그 이유는 드론이 움직일 수 있는 경우를 전부 구현하지 않았기 때문
# 전부 구현하지 않은 이유는 어차피 오른쪾 아래로 갈거면 오른쪽과 아래 방향으로 가는 경우만 
# 생각하면 될 거 같다는 그리디한 사고를 가지고 풀었음
# 왜 그랬는진 모르겠지만 지금 푸는 문제는 보드의 크기가 100으로 작게 제한사항이 있음
# 이렇게 제한 사항이 있기 때문에 전부 해보는 구현 문제에 해당함
# 따라서 그리디한 방법 말고 전부 탐색할 수 있도록 완탐으로 구현해야 할 것임
"""
def solution(board):
    answer = 0
    N = len(board)
    visited = []

    q = deque()
    q.append((0, 1, 'garo'))
    answer = -1
    while(q):
        # print("-"*50)
        answer += 1
        q_len = len(q)
        for _ in range(q_len):
            x, y, moyang = q.popleft()
            if (x,y,moyang) in visited:
                continue
            else:
                visited.append((x,y,moyang))
            # print("x=", x, "y=", y, moyang)
            if x == N-1 and y == N-1:
                return answer
            if moyang == 'garo':
                if x+1 < N > 0 and board[x+1][y-1] == 0 and board[x+1][y] == 0:
                    # -- -> 0:
                    # 00 -> 0:
                    q.append((x+1, y, 'sero'))
                    # -- -> :0
                    # 00 -> :0
                    q.append((x+1, y-1, 'sero'))
                    # -- -> 00
                    # 00 -> --
                    q.append((x+1, y, 'moyang'))
                if y+1 < N and board[x][y+1] == 0:
                    # --0 -> 0--
                    q.append((x, y+1, 'garo'))
            elif moyang == 'sero':
                if y+1 < N and board[x-1][y+1] == 0 and board[x][y+1] == 0:
                    # :0 -> --
                    # :0 -> 00
                    q.append((x-1, y+1, 'garo'))
                    # :0 -> 00
                    # :0 -> --
                    q.append((x, y+1, 'garo'))
                    # :0 -> 0:
                    # :0 -> 0:
                    q.append((x, y+1, 'sero'))
                if x+1 < N and board[x+1][y] == 0:
                    # : -> 0
                    # : -> :
                    # 0 -> :
                    q.append((x+1, y, 'sero'))
        q = deque(set(q))
    return answer
"""


board = [[0, 0, 0, 1, 1],
         [0, 0, 0, 1, 0],
         [0, 1, 0, 1, 1],
         [1, 1, 0, 0, 1],
         [0, 0, 0, 0, 0]]
print(solution(board))
