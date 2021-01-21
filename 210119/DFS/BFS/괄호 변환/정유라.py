from collections import deque
w = input()

data = []
l, r = 0, 0
temp = ""


# 올바른 문자열인지 확인
def check_right(u):
    count = 0
    for i in u:
        if i == "(":
            count += 1
        else:
            if count == 0:
                return False
            count -= 1
    return True
    

def change(w):
    global l, r, temp
    if len(w) == 0:
        return w
    for i in range(len(w)):
        if w[i] == '(':
            l += 1
        elif w[i] == ')':
            r += 1
        if l == r:
            u = w[:i+1]
            v = w[i+1:]
            print("l, r", u,v)

            if check_right(u) == True:
                u += change(v)
            else:
                temp += "("
                temp += change(v)
                print("after", temp)
                temp += ")"
                print("temp:", temp)
                print("for문 들어가기전 u, v", u,"|",v)
                for j in range(len(u)-2, 1, -1):
                    print("j:", j)
                    print("들어오면 안되지")
                    temp += u[j]
                return temp

            print(u, ",", v)


print(change(w))