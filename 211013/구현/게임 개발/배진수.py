n, m = map(int, input().split())
x, y, d = map(int, input().split())

game = []
for i in range(n):
    game.append(list(map(int, input().split())))

def make_direction(d):
    if d == 0:
        return 3
    else:
        return d-1
    
# 북 동 남 서
dx = [-1,0,1,0]
dy = [0,1,0,-1]

visit = set()
visit.add((x,y))
count = 0
while True:
    # print(x,y, count)
    if count == 4:
        break
    d = make_direction(d)
    mx = x + dx[d]
    my = y + dy[d]
    if 0<mx<n and 0<my<m:
        if game[mx][my] == 1:
            count += 1
        else:
            if (mx,my) not in visit:
                x, y = mx, my
                visit.add((x,y))
                count = 0
            else:
                count += 1

print(len(visit))
print(visit)