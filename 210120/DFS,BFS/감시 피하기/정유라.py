n = int(input())
graph = []
# n = 4
# graph = [
#     ['S','S','S','T'],
#     ['X','X','X','X'],
#     ['X','X','X','X'],
#     ['T','T','T','X']
# ]
# graph = [
#     ['X','S','X','X','T'],
#     ['T','X','S','X','X'],
#     ['X','X','X','X','X'],
#     ['X','T','X','X','X'],
#     ['X','X','T','X','X']
# ]
teacher = [] # 선생님들 위치
for i in range(n):
    graph.append(list(input().split()))
    for j in range(n):
        if graph[i][j] == 'T':
            teacher.append((i,j))

# print("teacher ---", teacher)


# 선생님이 방향에 따라 한 칸씩 이동하면서 확인
# 학생 찾으면 True/ 못 찾으면 False
def find_student(x, y, d):
    if d == 0: # 상
        while x >= 0:
            if graph[x][y] == 'O':
                return False
            elif graph[x][y] == 'S':
                return True
            else:
                x -= 1
    elif d == 1: # 하
        while x < n:
            if graph[x][y] == 'O':
                return False
            elif graph[x][y] == 'S':
                return True
            else:
                x += 1
    elif d == 2: # 좌
        while y >= 0:
            if graph[x][y] == 'O':
                return False
            elif graph[x][y] == 'S':
                return True
            else:
                y -= 1
    elif d == 3: # 우
         while y < n:
            if graph[x][y] == 'O':
                return False
            elif graph[x][y] == 'S':
                return True
            else:
                y += 1
    return False
    

# 각 선생님들 학생 잡으러 출발
# i : 0(상), 1(하), 2(좌), 3(우)
def process():
    for x, y in teacher:
        for i in range(4):
            if find_student(x, y, i): # 선생님이 학생 찾으면 True 반환
                return True
    # for문을 다 돌았다 : 못 찾았다
    return False

success = False
# dfs를 통해 재귀적으로 반복
# 장애물이 3개 설치될 때마다 선생님이 학생찾으러 감
def dfs(count):
    global success 
    if count == 3:
        if not process(): # process가 False일 때 학생을 못 찾았다는 것이므로
            success = True # 학생이 선생님 피하기 성공
            return                
        return 
        
        
    # 장애물 설치(연구소 문제 참고함)
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 'X':
                graph[i][j] = 'O'
                count += 1
                dfs(count)
                graph[i][j] = 'X'
                count -= 1
    
dfs(0)
if success == True:
    print("YES")
else:
    print("NO")