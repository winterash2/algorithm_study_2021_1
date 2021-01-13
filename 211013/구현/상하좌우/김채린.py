def solution(n, road):
    x=1
    y=1

    for i in road:
        if i=='R':
            y+=1
            if y>n:
                y-=1
        elif i=='L':
            y-=1
            if y<1:
                y+=1
        elif i=='U':
            x-=1
            if x<1:
                x+=1
        elif i=='D':
            x+=1
            if x>n:
                x-=1
    return x,y


x, y=solution(5, ['R', 'R', 'R', 'U', 'D', 'D'])
print(x, y)