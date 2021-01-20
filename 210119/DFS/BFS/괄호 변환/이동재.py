
def check_valid(p):
    check = 0
    for elem in p:
        if elem == '(':
            check += 1
        else:
            check -= 1
        if check < 0:
            return False
    if check == 0:
        return True
    else:
        return False


def make_u_v(w):
    u = ""
    v = ""
    check = 0
    done = False
    for elem in w:
        if done:
            v += elem
        else:
            u += elem
            if elem == '(':
                check += 1
            else:
                check -= 1
            if check == 0:
                done = True
    return [u, v]


def step(p):
    if p == "":
        return ""
    u, v = make_u_v(p)
    if check_valid(u):
        result = u + step(v)
    else:
        result = '('
        result += step(v)
        result += ')'
        print("result=", result)
        u = u[1:-1]
        u_reversed = ""
        for elem in u:
            # print(elem)
            if elem == "(":
                u_reversed += ')'
            elif elem == ")":
                u_reversed += '('
        result += u_reversed

    return result


def solution(p):
    answer = ''
    answer = step(p)
    return answer


p = "()))((()"
print(solution(p))
