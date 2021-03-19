from collections import deque


def solution(bridge_length, weight, truck_weights):
    answer = 0

    q = deque()
    cur_weight = 0
    time = 0
    for truck in truck_weights:
        time += 1
        if q and q[0][2] == time:  # 만약 트럭이 나가면 먼저 뺌
            cur_weight -= q[0][0]
            q.popleft()
        while cur_weight + truck > weight:  # 트럭이 들어갈 수 있을 때까지 앞에 있는 트럭들을 뺌
            w, s, e = q.popleft()
            cur_weight -= w
            time = e
        cur_weight += truck
        q.append((truck, time, time + bridge_length))  # (무게, 진입 시간, 나가는 시간)
    _, _, answer = q.pop()
    return answer


bridge_length = 2
weight = 10
truck_weights = [7, 4, 5, 6]
print(solution(bridge_length, weight, truck_weights))
