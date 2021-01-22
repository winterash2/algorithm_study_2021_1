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
    # u, v 나누기
    for i in range(len(w)):
        if w[i] == '(':
            l += 1
        elif w[i] == ')':
            r += 1
        if l == r:
            u = w[:i+1]
            v = w[i+1:]
            print("l, r", u,v)

            # 올바른 문자열이면 
            if check_right(u) == True:
                u += change(v)
            else:
                temp += "("
                temp += change(v)
                print("after", temp)
                temp += ")"
                print("temp:", temp)
                print("for문 들어가기전 u, v", u,"|",v)
                for i in range(len(u)):
                    if u[i] == '(':
                        u[i] = ')'
                    else:
                        u[i] = '('
                temp += "".join(u)
                return temp

            print(u, ",", v)


print(change(w))