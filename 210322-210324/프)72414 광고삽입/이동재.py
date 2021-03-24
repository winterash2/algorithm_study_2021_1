# 정확성  테스트
# 테스트 1 〉	통과 (3.44ms, 10.6MB)
# 테스트 2 〉	통과 (15.36ms, 11.3MB)
# 테스트 3 〉	통과 (32.10ms, 12.6MB)
# 테스트 4 〉	통과 (273.45ms, 27.9MB)
# 테스트 5 〉	통과 (439.12ms, 35.8MB)
# 테스트 6 〉	통과 (112.87ms, 13.2MB)
# 테스트 7 〉	통과 (873.81ms, 66.2MB)
# 테스트 8 〉	통과 (863.99ms, 65.9MB)
# 테스트 9 〉	통과 (1260.68ms, 90.1MB)
# 테스트 10 〉	통과 (1365.94ms, 90.3MB)
# 테스트 11 〉	통과 (1317.13ms, 90.6MB)
# 테스트 12 〉	통과 (1137.15ms, 81.6MB)
# 테스트 13 〉	통과 (1141.66ms, 90.4MB)
# 테스트 14 〉	통과 (1315.28ms, 80.2MB)
# 테스트 15 〉	통과 (42.65ms, 11.4MB)
# 테스트 16 〉	통과 (1138.87ms, 79.3MB)
# 테스트 17 〉	통과 (1460.49ms, 90.7MB)
# 테스트 18 〉	통과 (1160.51ms, 80.2MB)
# 테스트 19 〉	통과 (2.40ms, 10.5MB)
# 테스트 20 〉	통과 (5.24ms, 10.5MB)
# 테스트 21 〉	통과 (284.41ms, 26.9MB)
# 테스트 22 〉	통과 (307.80ms, 26.9MB)
# 테스트 23 〉	통과 (1319.19ms, 86.8MB)
# 테스트 24 〉	통과 (1209.35ms, 79.6MB)
# 테스트 25 〉	통과 (89.53ms, 12.4MB)
# 테스트 26 〉	통과 (45.45ms, 11.5MB)
# 테스트 27 〉	통과 (57.00ms, 12.2MB)
# 테스트 28 〉	통과 (55.70ms, 12.2MB)
# 테스트 29 〉	통과 (52.13ms, 11.9MB)
# 테스트 30 〉	통과 (38.35ms, 11.6MB)
# 테스트 31 〉	통과 (39.94ms, 11.6MB)
import heapq


def solution(play_time, adv_time, logs):
    logs_orig = [x for x in logs]
    answer = ''
    play_time = list(map(int, play_time.split(":")))
    play_time = play_time[0] * 3600 + play_time[1] * 60 + play_time[2]
    adv_time = list(map(int, adv_time.split(":")))
    adv_time = adv_time[0] * 3600 + adv_time[1] * 60 + adv_time[2]

    logs = []
    for log in logs_orig:
        start, end = log.split("-")
        start = list(map(int, start.split(":")))
        start = start[0] * 3600 + start[1] * 60 + start[2]
        end = list(map(int, end.split(":")))
        end = end[0] * 3600 + end[1] * 60 + end[2]
        logs.append((start, end))

    dp = [0 for _ in range(play_time)]
    logs.sort()
    idx = 0
    count = 0
    stack = []
    for i in range(play_time):
        while stack and stack[0] <= i:
            count -= 1
            heapq.heappop(stack)
        while idx < len(logs) and i == logs[idx][0]:
            count += 1
            heapq.heappush(stack, logs[idx][1])
            idx += 1
        dp[i] = count

    idx = 0
    count = 0
    for i in range(adv_time):
        count += dp[i]
    max_count = count
    for i in range(1, play_time - adv_time):
        count = count - dp[i]
        count = count + dp[adv_time + i]
        if count > max_count:
            max_count = count
            idx = i + 1

    answer = idx
    hh = answer // 3600
    mm = (answer % 3600) // 60
    ss = answer % 60
    answer = ''
    if hh < 10:
        answer += "0"
    answer += str(hh) + ":"
    if mm < 10:
        answer += "0"
    answer += str(mm) + ":"
    if ss < 10:
        answer += "0"
    answer += str(ss)

    return answer


play_time = "02:03:55"
adv_time = "00:14:15"
logs = ["01:20:15-01:45:14", "00:40:31-01:00:00",
        "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]

play_time = "00:01:00"
adv_time = "00:00:10"
logs = ["00:00:10-00:00:20"]

print(solution(play_time, adv_time, logs))



# 정확성  테스트
# 테스트 1 〉	통과 (3.65ms, 10.6MB)
# 테스트 2 〉	통과 (31.71ms, 11.4MB)
# 테스트 3 〉	통과 (52.86ms, 12.7MB)
# 테스트 4 〉	통과 (465.14ms, 28.2MB)
# 테스트 5 〉	통과 (396.48ms, 35.8MB)
# 테스트 6 〉	통과 (103.77ms, 13.1MB)
# 테스트 7 〉	통과 (1373.47ms, 66.2MB)
# 테스트 8 〉	실패 (시간 초과)
# 테스트 9 〉	실패 (시간 초과)
# 테스트 10 〉	실패 (시간 초과)
# 테스트 11 〉	실패 (시간 초과)
# 테스트 12 〉	통과 (1295.98ms, 81.6MB)
# 테스트 13 〉	실패 (시간 초과)
# 테스트 14 〉	실패 (시간 초과)
# 테스트 15 〉	통과 (42.23ms, 11.4MB)
# 테스트 16 〉	실패 (시간 초과)
# 테스트 17 〉	실패 (시간 초과)
# 테스트 18 〉	통과 (1150.48ms, 80.1MB)
# 테스트 19 〉	통과 (2.15ms, 10.6MB)
# 테스트 20 〉	통과 (1.71ms, 10.5MB)
# 테스트 21 〉	실패 (시간 초과)
# 테스트 22 〉	실패 (시간 초과)
# 테스트 23 〉	실패 (시간 초과)
# 테스트 24 〉	통과 (1246.99ms, 79.5MB)
# 테스트 25 〉	통과 (78.07ms, 12.4MB)
# 테스트 26 〉	통과 (44.15ms, 11.7MB)
# 테스트 27 〉	통과 (52.80ms, 12.2MB)
# 테스트 28 〉	통과 (54.81ms, 12.2MB)
# 테스트 29 〉	통과 (54.66ms, 11.7MB)
# 테스트 30 〉	통과 (36.01ms, 11.6MB)
# 테스트 31 〉	통과 (36.46ms, 11.6MB)
# 일부 시간 초과
"""
from bisect import bisect_left

def solution(play_time, adv_time, logs):
    logs_orig = [x for x in logs]
    answer = ''
    play_time = list(map(int, play_time.split(":")))
    play_time = play_time[0] * 3600 + play_time[1] * 60 + play_time[2]
    adv_time = list(map(int, adv_time.split(":")))
    adv_time = adv_time[0] * 3600 + adv_time[1] * 60 + adv_time[2]

    logs = []
    for log in logs_orig:
        start, end = log.split("-")
        start = list(map(int, start.split(":")))
        start = start[0] * 3600 + start[1] * 60 + start[2]
        end = list(map(int, end.split(":")))
        end = end[0] * 3600 + end[1] * 60 + end[2]
        logs.append((start, end))

    dp = [0 for _ in range(play_time)]
    logs.sort()
    idx = 0
    count = 0
    stack = []
    for i in range(play_time):
        while stack and stack[0] <= i:
            count -= 1
            stack = stack[1:]
        while idx < len(logs) and i == logs[idx][0]:
            count += 1
            stack.insert(bisect_left(stack, logs[idx][1]), logs[idx][1])
            idx += 1
        dp[i] = count

    idx = 0
    count = 0
    for i in range(adv_time):
        count += dp[i]
    max_count = count
    for i in range(1, play_time - adv_time):
        count = count - dp[i]
        count = count + dp[adv_time + i]
        if count > max_count:
            max_count = count
            idx = i + 1

    answer = idx
    hh = answer // 3600
    mm = (answer % 3600) // 60
    ss = answer % 60
    answer = ''
    if hh < 10:
        answer += "0"
    answer += str(hh) + ":"
    if mm < 10:
        answer += "0"
    answer += str(mm) + ":"
    if ss < 10:
        answer += "0"
    answer += str(ss)

    return answer
"""