# http://programmers.co.kr/learn/courses/30/lessons/17676

# 19:00 start
# 19:17 문제 이해함..


# 1. 리스트에 시작, 끝 시간들 삽입 -> sort
# 2. 시작 시간부터 1초씩 끊어서 그 안에 큐의 시간들이 해당되는지 -> 해당되면 cnt+1

from datetime import datetime, timedelta

def compare(time, end_time):
    start = time
    end = start + timedelta(milliseconds=999)
    if end > end_time:
        return -1
    cnt = 0
    
    for t in time_list:
        if start <= t and t <= end:
            cnt += 1

    return cnt

time_list = []
def solution(lines):
    answer = 0
    
    for time in lines:
        # print(time.split())
        temp = time.split(' ') # => ['2016-09-15', '01:00:04.001', '2.0s']
        date = str(temp[0]) + " " + str(temp[1]) # => 2016-09-15 01:00:04.001
        
        if '.' in temp[2]:
            result_time = temp[2][:-1].split(".")
        else:
            result_time = [temp[2][:-1], 0]

        end = datetime.fromisoformat(date)
        start = end - timedelta(seconds=int(result_time[0]), milliseconds=int(result_time[1]) - 1) 
        time_list.append(start)
        time_list.append(end)
        time_list.sort()

    
    for start_time in time_list:
        if start_time < datetime.fromisoformat("2016-09-15 00:00:00.000"):
            continue
        compare_time = start_time
        break
    
    compare_end = time_list[-1]
    while True:
        
        count = compare(compare_time, compare_end)
        if count == -1:
            break
        answer = max(answer, count)
        compare_time += timedelta(milliseconds=999)
        


    return answer

# print(solution([
#     "2016-09-15 20:59:57.421 0.351s",
#     "2016-09-15 20:59:58.233 1.181s",
#     "2016-09-15 20:59:58.299 0.8s",
#     "2016-09-15 20:59:58.688 1.041s",
#     "2016-09-15 20:59:59.591 1.412s",
#     "2016-09-15 21:00:00.464 1.466s",
#     "2016-09-15 21:00:00.741 1.581s",
#     "2016-09-15 21:00:00.748 2.31s",
#     "2016-09-15 21:00:00.966 0.381s",
#     "2016-09-15 21:00:02.066 2.62s"
# ]))

# print(solution([
# "2016-09-15 01:00:04.001 2.0s",
# "2016-09-15 01:00:07.000 2s"
# ]))

# print(solution(["2016-09-15 00:00:00.000 2.3s", "2016-09-15 23:59:59.999 0.1s"]))
print(solution(["2016-09-15 00:00:00.000 3s", "2016-09-15 00:00:00.001 2s", "2016-09-15 00:00:00.002 1s"]))
