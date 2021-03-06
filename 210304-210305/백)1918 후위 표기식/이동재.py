# 3차 시도 성공
# 자꾸 틀렸던 이유는 앞에서는 A+B*C 이렇게 연달아 나오는게 제대로 처리가 안 되었었음
string = list(input())


def conversion(string):
    gualho = False
    # 괄호 먼저 다 제거
    while True:
        exist = False
        depth = 0
        start = -1
        end = -1
        for i in range(len(string)):
            if string[i] is not list and string[i] == '(':
                gualho = True
                exist = True
                depth += 1
                if start == -1:
                    start = i
            elif string[i] is not list and string[i] == ')':
                depth -= 1
                if depth == 0:
                    end = i
                    string = string[:start] + \
                        conversion(string[start+1:end]) + string[end+1:]
                    break
        if not exist:
            break

    if len(string) == 1:
        return string

    # print("string", string)
    pre = ''
    oper = ''
    suf = ''
    stack = []
    if len(string) >= 3:
        # 곱셈, 나눗셈을 먼저 다 처리
        for s in string:
            stack.append(s)
            if len(stack) >= 3:
                if stack[-2] == '*' or stack[-2] == '/':
                    pre = stack[-3]
                    oper = stack[-2]
                    suf = stack[-1]
                    del(stack[-3:])
                    stack.append('' + pre + suf + oper)
        string = stack
        stack = []
        # 그 다음 덧셈, 뺄셈을 처리
        for s in string:
            stack.append(s)
            if len(stack) >= 3:
                if stack[-2] == '+' or stack[-2] == '-':
                    pre = stack[-3]
                    oper = stack[-2]
                    suf = stack[-1]
                    del(stack[-3:])
                    stack.append('' + pre + suf + oper)

    # print("stack", stack)
    return stack


print(conversion(string)[0])

# 2차 시도, 틀렸다고 나오는데 왜 틀린지 모르겠음
"""
def conversion(string):
    if len(string) == 1:
        return string
    pre = []
    suf = []
    oper = ''
    if string[0] != '(':
        pre = string[0]
        oper = string[1]
        suf = string[2:]
    else:
        depth = 0
        for i in range(len(string)):
            if string[i] == '(':
                depth += 1
            elif string[i] == ')':
                depth -= 1
                if depth == 0:
                    pre = string[1:i]
                    if i != len(string) - 1:
                        oper = string[i+1]
                        suf = ''.join(string[i+2:])
                    break
    if oper == '':
        return conversion(pre)
    else:
        return conversion(pre) + conversion(suf) + oper


print(conversion(input()))
"""

# 1차 시도, 틀렸다고 나오는데 왜 틀린지 모르겠음
"""
orig = list(input())


def conversion(string):
    # print("|", string, "|")
    operators = ['+', '-', '*', '/']
    a = ''
    b = ''
    oper = ''
    depth = 0
    for i in range(len(string)):
        if string[i] == '(':
            depth += 1
            if depth == 1:
                continue
        elif string[i] == ')':
            depth -= 1
            if depth == 0:
                continue

        if depth > 0:
            a += string[i]
        elif string[i] in operators:
            oper = string[i]
            b = string[i+1:]
            if b[0] == '(':
                b = b[1:-1]
                b = ''.join(b)
            break
        else:
            a += string[i]
    if oper == '':
        if len(a) == 1:
            return a
        else:
            return conversion(a)
    else:
        return conversion(a) + conversion(b) + oper


print(conversion(orig))
"""
