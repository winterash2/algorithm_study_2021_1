import sys
input = sys.stdin.readline

x, y, w, h = map(int, input().split())
rect_x = [0]
rect_y = [0]
rect_x.append(w)
rect_y.append(h)

answer = int(1e9)
for i in range(2):
    answer = min(answer, abs(x - rect_x[i]), abs(y - rect_y[i]))
print(answer)

"""
그냥 이거한줄이면 된다,,, 난 바보
print(min(x,y,(w-x),(h-y)))
"""