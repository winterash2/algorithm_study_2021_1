# 예제 다 통과하는데 왜 틀릴까ㅠㅠ
import sys
input = sys.stdin.readline

n = int(input())
wall = []
for i in range(n):
    wall.append(list(map(int, input().split())))

tail = [0,0]
head = [0,1]
cnt = 0

def bfs(tail, head):
    global cnt
    if wall[head[0]][head[1]] == 1:
        return
    if head == [n-1,n-1]:
        cnt += 1
        return
    else:
        if tail[0] == head[0]:
            if head[1] == (n-1):
                return
            if wall[head[0]][head[1]+1] == 1:
                return
            if head[0] == (n-1):
                bfs([head[0], head[1]], [head[0], head[1]+1])
            else:
                bfs([head[0], head[1]], [head[0], head[1]+1])
                if wall[head[0]+1][head[1]] == 1:
                    return
                bfs([head[0], head[1]], [head[0]+1, head[1]+1])
        elif tail[1] == head[1]:
            if head[0] == (n-1):
                return
            if head[1] == (n-1):
                bfs([head[0], head[1]], [head[0]+1, head[1]])
            else:
                bfs([head[0], head[1]], [head[0]+1, head[1]])
                if wall[head[0]+1][head[1]] == 1:
                    return
                bfs([head[0], head[1]], [head[0]+1, head[1]+1])
        else:
            if head[0] == (n-1):
                bfs([head[0], head[1]], [head[0], head[1]+1])
            elif head[1] == (n-1):
                bfs([head[0], head[1]], [head[0]+1, head[1]])
            else:
                bfs([head[0], head[1]], [head[0], head[1]+1])
                bfs([head[0], head[1]], [head[0]+1, head[1]])
                if wall[head[0]+1][head[1]] == 1:
                    return
                bfs([head[0], head[1]], [head[0]+1, head[1]+1])

bfs(tail, head)
print(cnt)
