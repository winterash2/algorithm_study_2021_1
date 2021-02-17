from collections import deque

n, m = map(int, input().split())

move = [-1, 1, 2]
answer = 0
visit = []
fast = int(1e9)
time = 0
q = deque()
q.append((n, time))
# cnt = 0
while q:
    # cnt += 1
    value, tt = q.popleft()
    visit.append(value)
    if tt > fast:
        break
    if value == m:
        answer += 1
        fast = tt
    for i in range(3):
        if i == 2:
            nn = value * move[i]
        else:
            nn = value + move[i]
        if nn in visit:
            continue
        if 0 <= nn <= 100000:
            q.append((nn, tt + 1))

print(fast)
print(answer)
# print(cnt)
