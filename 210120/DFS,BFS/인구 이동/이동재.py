from collections import deque
# from pprint import pprint as pprint
import sys
input = sys.stdin.readline

# N, L, R = map(int, input().split())
# map_org = []
# for _ in range(N):
#     map_org.append(list(map(int, input().split())))

# N, L, R = 2, 20, 50
# map_org = [[50, 30], [20, 40]]
# map_check = [[0] * N for _ in range(N)]

N, L, R = 4,10,50
map_org = [
    [10, 100, 20, 90],
    [80, 100, 60, 70],
    [70, 20, 30, 40],
    [50, 20, 100, 10]
    ]
map_check = [[0] * N for _ in range(N)]


def unite(x, y):
    global map_org, map_check
    directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    q = deque([(x,y)])
    group = [(x,y)]
    total_population = 0
    map_check[x][y] = 1
    while q:
        x, y = q.popleft()
        total_population += map_org[x][y]
        for dx, dy in directions:
            nx = x + dx
            ny = y + dy
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if map_check[nx][ny] != 0:
                continue
            # print("nx,ny=",nx,ny)
            # print("d[0],d[1]=",d[0], d[1])
            if L <= abs(map_org[x][y] - map_org[nx][ny]) <= R:
                map_check[nx][ny] = 1
                q.append((nx, ny))
                group.append((nx, ny))
    # print(sorted(group))
    # pprint(map_check, width=20)
    if len(group) == 1:
        return False
    else:
        div_population = total_population // len(group)
        for x, y in group:
            map_org[x][y] = div_population
        return True


count = 0
while True:
    # print("-"*50)
    map_check = [[0] * N for _ in range(N)]
    is_united = False
    for x in range(N):
        for y in range(N):
            if map_check[x][y] == 0:
                is_united = True if unite(x, y) or is_united else False
    if not is_united:
        break
    else:
        count += 1

print(count)

# 시간 초과 뜨긴 하는데 책 모범답안도 시간초과 뜸
# 아래 코드는 백준에 파이썬으로 푼 사람 중 가장 빠르게 푼 사람 코드임
# 기본적인 문제 풀이 방식은 동일하나 이 사람의 경우 처음 한 번은 x*y 배열을 전부 돌지만
# 그 다음부터는 숫자가 변경된 애들로만 국경선 공유를 시작하도록 함
import sys
from collections import deque
r=sys.stdin.readline
N,L,R=map(int,r().split())
A=list()
for _ in range(N):
    A.append(list(map(int,r().split())))
def bfs(x,y):
    q=deque([(x,y)])
    union=[(x,y)]
    ck[x][y]=1
    while q:
        x,y=q.popleft()
        for dx,dy in [(1,0),(0,1),(-1,0),(0,-1)]:
            nx,ny=x+dx,y+dy
            if not 0<=nx<N or not 0<=ny<N:continue
            if ck[nx][ny]==1:continue
            if L<=abs(A[x][y]-A[nx][ny])<=R:
                union.append((nx,ny))
                ck[nx][ny]=1
                q.append((nx,ny))
    if len(union)>1:
        population=sum(map(lambda x: A[x[0]][x[1]],union)) // len(union)
        for x,y in union:
            A[x][y]=population
            nextQ.append((x,y))
        return True
    return False
cnt=0
nextQ=deque() # 이 nextQ를 이용하여 이전에 인구수의 변화가 있었던 애들로부터만 그 다음 회차 이동을 결정하게 함
for i in range(N):
    for j in range(N):
        nextQ.append((i,j))
while True:
    flg=False
    ck=[[0]*N for _ in range(N)]
    size=len(nextQ)
    for _ in range(size):
        i,j=nextQ.popleft()
        if ck[i][j]:continue
        if bfs(i,j):
            flg=True
    if flg: cnt+=1
    if not flg:
        print(cnt)
        exit(0)