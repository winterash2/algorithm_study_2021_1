ss = input()
bomb = input()
stack = []
bomb_len = len(bomb)
for s in ss:
    stack.append(s)
    if s == bomb[-1] and ''.join(stack[-bomb_len:]) == bomb:
        del stack[-bomb_len:]
res = ''.join(stack)

if res:
    print(res)
else:
    print("FRULA")