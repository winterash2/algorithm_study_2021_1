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
teacher = []
for i in range(n):
    graph.append(list(input().split()))
    for j in range(n):
        if graph[i][j] == 'T':
            teacher.append((i,j))

# print("teacher ---", teacher)


def find_student(x, y, d):
    # print("--in find_student --")
    # print("x:",x,"y:",y,"d:",d)
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
            # print("x,y:",x,y)
            if graph[x][y] == 'O':
                return False
            elif graph[x][y] == 'S':
                # print("여기 들어올텐데?")
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
    
        
def process():
    for x, y in teacher:
        for i in range(4):
            if find_student(x, y, i):
                # print(x,y,i)
                return True
    return False

find = False
def dfs(count):
    global find
    if count == 3:
        # for i in graph:
        #     print(i)
        if not process():
            find = True
            return                
        return 
        
        

    for i in range(n):
        for j in range(n):
            if graph[i][j] == 'X':
                graph[i][j] = 'O'
                count += 1
                dfs(count)
                graph[i][j] = 'X'
                count -= 1
    
dfs(0)
if find == True:
    print("YES")
else:
    print("NO")