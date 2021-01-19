from collections import deque

n, m, k, x = map(int, input().split())
city = [[] for _ in range(n+1)]
city[0] = [0]
count = [-1] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    city[a].append(b)

q = deque()
q.append(x)
count[x] = 0

while q:
    node = q.popleft()
    for c in city[node]:
        if count[c] == -1:
            count[c] = count[node] + 1
            q.append(c)

# print(count)
result = False
for i in range(len(count)):
    if count[i] == k:
        result = True
        print(i)

if result is not True:
    print(-1)