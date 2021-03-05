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
