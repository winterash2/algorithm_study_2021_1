# 2차 시도, 틀렸다고 나오는데 왜 틀린지 모르겠음
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


string = input()
print(conversion(string))


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
