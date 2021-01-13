n = int(input())
move_plan = list(map(str, input().split()))

ny = [-1,1,0,0]
nx = [0,0,-1,1] 
move = ['L','R','U','D']

x = 0
y = 0
for plan in move_plan:
    for i in range(len(move)):
        if plan == move[i]:
            mx = x + nx[i]
            my = y + ny[i]
    if mx < 0 or mx > (n-1) or my < 0 or my > (n-1):
        continue
    x, y = mx, my
    print(x,y)

print(x+1, y+1)