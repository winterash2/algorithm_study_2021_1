from collections import deque

N, M = [int(x) for x in input().split()]
maze = []
for _ in range(N):
    maze.append([int(x) for x in input()])

direction = [[-1, 0], [1, 0], [0, -1], [0, 1]]  # 상하좌우

# N, M = 5, 6
# maze = [[1, 0, 1, 0, 1, 0], [1, 1, 1, 1, 1, 1], [
#     0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]]


def bfs(x, y):
    global N, M, maze

    q = deque()
    q.append((x, y))
    while q:
        curr = q.popleft()

        for d in direction:
            nx = curr[0] + d[0]
            ny = curr[1] + d[1]
            if nx >= 0 and nx < N and ny >= 0 and ny < M:  # 다음 위치가 배열 범위를 넘어가지 않을 때
                if maze[nx][ny] == 0:  # 괴물이 있는 부분이면
                    pass
                elif maze[nx][ny] == 1:  # 아직 한 번도 안 간 곳이면
                    maze[nx][ny] = maze[curr[0]][curr[1]] + 1
                    q.append((nx, ny))
                else:  # 2보다 큰 때니까 한 번 이상 갔던 곳일 때
                    if maze[nx][ny] > maze[curr[0]][curr[1]] + 1:  # 한 번 갔었는데 지금 가면 더 빠르게 갈 수 있는 경우
                        maze[nx][ny] = maze[curr[0]][curr[1]] + 1
                        q.append((nx, ny))


bfs(0, 0)
print(maze[N-1][M-1])

# 재귀로 풀면 코드가 더 짧아질거 같아서 함 해봤음
# 코드는 좀 더 짧아진거 같은데 대신 시간초과 뜸
# 파이썬에서 어떤 문제를 재귀로 풀려고 할 때 재귀의 반복 회수가 아주 작음을 알아야 함
# 아래 코드 2줄이 재귀 반복횟수를 늘려주는 코드임
"""
import sys  
sys.setrecursionlimit(10**8)
def search(maze, i, j, count):
    # 맵 바깥이면 수행 X
    if i < 0 or i >= N or j < 0 or j >= M:
        return
    # 괴물이 있는 위치면 수행 X
    elif maze[i][j] == 0:
        return

    if maze[i][j] == 1:
        maze[i][j] = count
        for d in direction:
            search(maze, i+d[0], j+d[1], count+1)
    if count < maze[i][j]:
        maze[i][j] = count
        for d in direction:
            search(maze, i+d[0], j+d[1], count+1)
    else:
        return
search(maze, 0, 0, 1)
print(maze[N-1][M-1])
"""
