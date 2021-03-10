# http://boj.kr/1918
s = list(input())

# 1. 피연산자면 그대로 출력
# 2. 연산자인 경우
#   1) ')'인 경우 '('가 나올때까지 스택에 있는 것들 모두 pop
#   2) 빈 스택인 경우 스택에 push
#   3) 위 경우가 모두 아닌 연산자인 경우 들어있는 스택의 연산자와 우선순위 비교 후 스택에 있는 연산자의 우선순위가 높으면 pop하여 출력, 반대면 연산자를 스택에 push

operator = {
    '*': 3,
    '/': 3,
    '+': 2,
    '-': 2, 
    '(': 1
}

stack = []
result = []


for c in s:
    # 괄호처리
    if c == '(':
        stack.append(c)
    
    # 연산자인 경우
    elif c in '+-/*':
        # 스택이 비어있는 경우
        if len(stack) == 0:
            stack.append(c)

        else:
            # 우선순위 비교
            # 왜 스택빌때까지. . .? 
            while stack:
                if operator[stack[-1]] >= operator[c]:
                    temp = stack.pop()
                    result.append(temp)
                else:
                    break
            stack.append(c)

    # 괄호처리
    elif c == ')':
        while True:
            tmp = stack.pop()
            if tmp == '(':
                break
            result.append(tmp)
    
    # 피연산자인 경우
    else:
        result.append(c)
    
# A*B-C+D*E*F/G-(H+I)
            

while len(stack) > 0:
    result.append(stack.pop())

print(''.join(result))
