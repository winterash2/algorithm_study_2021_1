# http://programmers.co.kr/learn/courses/30/lessons/17676

# 19:00 start
# 19:17 문제 이해함..


# 1. 우선순위 큐에 시작, 끝 시간들 삽입
# 2. 시작 시간부터 1초씩 끊어서 그 안에 큐의 시간들이 해당되는지 -> 해당되면 cnt+1

import heapq

def solution(lines):
    answer = 0
    q = []
    for time in lines:
        h, m, s = time.split()[1].split(":")
        # s, ms = s.split(".")
        res_time = time.split()[2][:-1]
        s, res_time = float(s), float(res_time)
        print("s, res time", s, res_time)
        print("subtract:", s- res_time)
        # h, m, s, ms, res_time = int(h), int(m), int(s), int(ms), float(res_time)
        print(res_time)
        print(h, m, s, ms)

        # if ms - res_time < 0:
        #     ms+
        heapq.heappush(q, (h, m, s, ms))

    print(q)

    return answer

print(solution([
    "2016-09-15 20:59:57.421 0.351s",
    "2016-09-15 20:59:58.233 1.181s",
    "2016-09-15 20:59:58.299 0.8s",
    "2016-09-15 20:59:58.688 1.041s",
    "2016-09-15 20:59:59.591 1.412s",
    "2016-09-15 21:00:00.464 1.466s",
    "2016-09-15 21:00:00.741 1.581s",
    "2016-09-15 21:00:00.748 2.31s",
    "2016-09-15 21:00:00.966 0.381s",
    "2016-09-15 21:00:02.066 2.62s"
]))
