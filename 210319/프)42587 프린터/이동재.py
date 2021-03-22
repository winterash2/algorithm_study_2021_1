from collections import deque

def solution(priorities, location):
    answer = 0
    # 먼저 뒤에서부터 봤을 때의 최대 우선순위를 구함
    q = deque()
    for i in range(len(priorities)):
        q.append((priorities[i], True if i == location else False))
    while q:
        answer += 1
        maxVal = max(q)[0]
        while True:
            cur = q.popleft()
            if cur[0] == maxVal:
                break
            else:
                q.append(cur)
        if cur[1]:
            break
    return answer

priorities = [2, 1, 3, 2]
location = 2
priorities = [1, 1, 9, 1, 1, 1]
location = 0
print(solution(priorities, location))