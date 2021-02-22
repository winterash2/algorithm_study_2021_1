# 이렇게 간단한걸... 300ms...
# 자괴감 최대로...
string = input()
bomb = input()

char = bomb[-1]
stack = []
n = len(bomb)

for c in string:
    stack.append(c)
    if c == char and ''.join(stack[-n:]) == bomb:
        del stack[-n:]

ans = ''.join(stack)
if ans:
    print(ans)
else:
    print('FRULA')

# 좋은 테스트 케이스
"""
1212ab112ab2abab
12ab
"""

# 어떻게든 내가 푼 것
# 성공은 했는데 1296ms...
"""
from collections import deque

orig = [x for x in input()]
boom = [x for x in input()]

if len(boom) == 1:
    while True:
        try:
            orig.remove(boom[0])
        except:
            break
    answer = ''.join(orig)
else:
    used = deque()
    notUsed = deque()
    for i in range(len(orig)-1, -1, -1):
        notUsed.append(orig[i])

    cnt = 0
    while notUsed:
        # print(used, cnt)
        cur = notUsed.pop()
        used.append(cur)
        if cur == boom[0]:
            cnt = 1
        elif cur == boom[cnt]:
            cnt += 1
            if cnt == len(boom):
                for _ in range(cnt):
                    remove = used.pop()
                for _ in range(len(boom)):
                    try:
                        notUsed.append(used.pop())
                    except:
                        break
                cnt = 0
        else:
            cnt = 0

    answer = ''
    while used:
        answer += used.popleft()

if answer == '':
    print('FRULA')
else:
    print(answer)
"""

# 시간초과
"""
orig = [x for x in input()]
boom = [x for x in input()]
boomLen = len(boom)

idx = 0
cnt = 0
i = 0
while True:
    print("i=",i)
    if i >= len(orig):
        break
    if orig[i] == '':
        pass
    elif orig[i] == boom[0]:
        idx = i
        cnt = 1
    elif orig[i] == boom[cnt]:
        cnt += 1
        if cnt == boomLen:
            i = -1
            while True:
                if orig[idx] != '':
                    orig[idx] = ''
                    cnt -= 1
                    if cnt == 0:
                        break
                idx += 1
    else:
        cnt = 0
    i += 1

answer = ''.join(orig)
if answer == '':
    print('FRULA')
else:
    print(answer)
"""
