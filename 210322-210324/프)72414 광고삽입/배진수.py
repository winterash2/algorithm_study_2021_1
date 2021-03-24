def solution(play_time, adv_time, logs):
    answer = ''
    
    return answer

# import datetime


# def string_to_datetime(s):
#     h, m, s = s.split(":")
#     h = zero_remove(h)
#     m = zero_remove(m)
#     s = zero_remove(s)
#     s_time = datetime.time(int(h), int(m), int(s))
#     return s_time


# def zero_remove(x):
#     if x[0] == "0":
#         return x[1]
#     else:
#         return x


# def solution(play_time, adv_time, logs):
#     answer = ''
#     play_time = string_to_datetime(play_time)
#     adv_time = string_to_datetime(play_time)

#     log_list = []
#     for log in logs:
#         start, end = log.split("-")
#         start_time = string_to_datetime(start)
#         end_time = string_to_datetime(end)
#         log_list.append((start_time, end_time))
    

#     return answer


logs = ["01:20:15-01:45:14", "00:40:31-01:00:00",
        "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]
adv_time = "00:14:15"
play_time = "02:03:55"

logs = ["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]
adv_time = "25:00:00"
play_time = "99:59:59"
solution(play_time, adv_time, logs)
