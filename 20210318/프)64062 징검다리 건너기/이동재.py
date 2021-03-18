def ispossible(stones, k, val):
    possible = True
    count = 0
    for stone in stones:
        if stone - val <= 0:
            count += 1
        else:
            count = 0
        if count >= k:
            possible = False
            break
    return possible


def solution(stones, k):
    answer = 0
    start = 1
    end = 200000000
    while start <= end:
        mid = (start + end) // 2
        if ispossible(stones, k, mid):
            answer = max(answer, mid)
            start = mid + 1
        else:
            end = mid - 1
    return answer + 1 # 밟으면서 지나가서 통과하는 마지막 경우가 있기 때문에 +1


stones = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1]
k = 3
print(solution(stones, k))


"""
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
    nomore = False
    while q:
        depth, idx = heapq.heappop(q)
        if answer != depth:
            if nomore:
                break
            answerPrev = answer
            answer = depth
        idxPrev = find(parent, idx-1)
        if idx - idxPrev > k: # 앞을 체크함, 여기서 걸린다는 것은 현재꺼를 밟을 수 없다는 의미
            answer = answerPrev
            break
        union(parent, idx, idx-1)
        end = idx + k + 1 if idx + k < l else l
        for i in range(idx, end):
            if i - find(parent, i) > k:
                nomore = True
        # print(parent)
    
    return answer
"""
