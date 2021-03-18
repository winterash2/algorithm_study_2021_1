import heapq


def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def solution(stones, k):
    answer = 0
    parent = [i for i in range(len(stones)+1)]
    l = len(stones) + 1
    q = []
    for i in range(len(stones)):
        q.append((stones[i], i+1))
    heapq.heapify(q)
    answer = 0
    answerPrev = 0
    while q:
        depth, idx = heapq.heappop(q)
        if answer != depth:
            answerPrev = answer
            answer = depth
        idxPrev = find(parent, idx-1)
        if idx - idxPrev >= k:
            answer = answerPrev
            break
        union(parent, idx, idx-1)
        # print(parent)
    
    return answer

stones = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1]
k = 3
print(solution(stones, k))