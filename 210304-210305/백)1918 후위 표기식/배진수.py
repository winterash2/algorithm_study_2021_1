# 왜 틀린지 모름 ㅡㅡ
ss = input()

stack = []
stack_kiho = []
cnt = 0
for s in ss:
    if ord('A') <= ord(s) <= ord('Z'):
        stack.append(s)
    elif s == '+' or s == '-':
        if stack_kiho and cnt == 0:
            if stack_kiho[-1] == '*' or stack_kiho[-1] == '/':
                while stack_kiho:
                    stack.append(stack_kiho.pop())
        stack_kiho.append(s)
    elif s == '*' or s == '/':
        stack_kiho.append(s)
    elif s == '(':
        cnt += 1
    elif s == ')':
        cnt -= 1
        if cnt == 0:
            while stack_kiho:
                stack.append(stack_kiho.pop())
while stack_kiho:
    stack.append(stack_kiho.pop())
result = ''.join(stack)
print(result)
