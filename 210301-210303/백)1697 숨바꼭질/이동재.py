from collections import deque

N, K = map(int, input().split())
visited = [False for _ in range(200000)]

q = deque()
q.append(N)
answer = 0
while q:
    answer += 1
    for _ in range(len(q)):
        cur = q.popleft()
        if cur == K:
            break
        if cur < 0 or cur >= 200000 or visited[cur]:
            continue
        visited[cur] = True
        q.append(cur-1)
        q.append(cur+1)
        q.append(cur*2)
    if cur == K:
        break

print(answer-1)