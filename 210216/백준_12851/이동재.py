# dict로 시도(시간초과)

N, K = map(int, input().split())
MAX = K + abs(N-K)
prevDict = {N: 1}
nextDict = dict()
prev_visit = [False for _ in range(MAX)]
next_visit = [False for _ in range(MAX)]

count = 0
while True:
    # print(prevDict)
    try:
        answer = prevDict[K]
        break
    except:
        count += 1
        for key in prevDict:
            if prev_visit[key]:
                continue
            next_visit[key] = True
            try:
                nextDict[key-1] += prevDict[key]
            except:
                if key-1 >= 0:
                    nextDict[key-1] = prevDict[key]
            try:
                nextDict[key+1] += prevDict[key]
            except:
                if key+1 <= MAX:
                    nextDict[key+1] = prevDict[key]
            try:
                nextDict[key*2] += prevDict[key]
            except:
                if key*2 <= MAX:
                    nextDict[key*2] = prevDict[key]
        prev_visit = next_visit
        next_visit = [i for i in prev_visit]
    prevDict = nextDict
    nextDict = dict()
    print(prevDict)

print(count)
print(answer)


# 큐로 시도해본 것(메모리 초과)
"""
N, K = map(int, input().split())
q = deque()
qc = deque()
q.append(N, 1)
diff = -1
while q.count(K) == 0:
    diff += 1
    for _ in range(len(q)):
        curr = q.popleft()
        if curr >= K * 2:
            continue
        q.append(curr+1)
        q.append(curr-1)
        q.append(curr*2)

print(diff+1)
print(q.count(K))
"""

"""
import copy
# 배열로 시도해본 것(시간 초과)

N, K = map(int, input().split())
MAX = abs(N - K) * 2
prev_list = [0 for _ in range(MAX)]
prev_list[N] = 1
next_list = [0 for _ in range(MAX)]
prev_visit = [False for _ in range(MAX)]
next_visit = [False for _ in range(MAX)]

diff = 0
while prev_list[K] == 0:
    diff += 1
    for i in range(MAX):
        if prev_list[i] != 0:
            if prev_visit[i]:
                continue
            next_visit[i] = True
            if i-1 >= 0:
                next_list[i-1] += prev_list[i]
            if i+1 < MAX:
                next_list[i+1] += prev_list[i]
            if i*2 < MAX:
                next_list[i*2] += prev_list[i]
    prev_list = next_list
    next_list = [0 for _ in range(MAX)]
    prev_visit = next_visit
    next_visit = copy.copy(prev_visit)
    # print(prev_list)

print(diff)
print(prev_list[K])
"""
