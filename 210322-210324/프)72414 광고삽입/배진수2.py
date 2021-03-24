def m_sec(time):
    h, m, s = time.split(':')
    return (int(h) * 60 * 60 + int(m) * 60 + int(s))


def m_time(time):
    ans = ""
    hour = time // 3600
    h = str(hour).zfill(2)
    min = (time % 3600) // 60
    m = str(min).zfill(2)
    sec = (time % 3600) % 60
    s = str(sec).zfill(2)
    ans = h + ":" + m + ":" + s
    return ans


"""
def solution(play_time, adv_time, logs):
    log_time = []

    if adv_time == play_time:
        return "00:00:00"

    for adv in logs:
        first, second = adv.split('-')
        start = m_sec(first)
        end = m_sec(second)
        log_time.append((start, end))

    log_time.sort()
    result = [0] * len(log_time)

    ptime = m_sec(play_time)
    x = m_sec(adv_time)
    res = 0
    answer = 0
    for i in range(len(result)):
        st, en = log_time[i]
        start_time = st
        end_time = st + x
        for tmp_time in log_time:
            tmp_start, tmp_end = tmp_time
            if tmp_start > end_time:
                break

            if start_time <= tmp_start <= end_time and tmp_end <= end_time:
                result[i] += (tmp_end - tmp_start)
            elif start_time <= tmp_start <= end_time and tmp_end > end_time:
                result[i] += (end_time - tmp_start)
            elif tmp_start <= start_time and tmp_end >= end_time:
                result[i] += (end_time - start_time)
            elif tmp_start <= start_time and start_time <= tmp_end <= end_time:
                result[i] += (tmp_end - start_time)
        if result[i] > res:
            res = result[i]
            answer = start_time
    return m_time(answer)
"""


def m_sec(time):
    h, m, s = time.split(':')
    return (int(h) * 60 * 60 + int(m) * 60 + int(s))


def m_time(time):
    ans = ""
    hour = time // 3600
    h = str(hour).zfill(2)
    min = (time % 3600) // 60
    m = str(min).zfill(2)
    sec = (time % 3600) % 60
    s = str(sec).zfill(2)
    ans = h + ":" + m + ":" + s
    return ans


def solution(play_time, adv_time, logs):
    log_time = []

    if adv_time == play_time:
        return "00:00:00"
    aa = set()
    for adv in logs:
        first, second = adv.split('-')
        start = m_sec(first)
        end = m_sec(second)
        log_time.append((start, end))
        aa.add(start)

    result = [0] * len(aa)

    ptime = m_sec(play_time)
    x = m_sec(adv_time)
    res = 0
    answer = 0
    aa = list(aa)
    # aa.sort()
    log_time.sort()
    for i in range(len(aa)):
        st = aa[i]
        start_time = st
        end_time = st + x
        for tmp_time in log_time:
            tmp_start, tmp_end = tmp_time
            if tmp_start > end_time:
                break

            if start_time <= tmp_start <= end_time and tmp_end <= end_time:
                result[i] += (tmp_end - tmp_start)
            elif start_time <= tmp_start <= end_time and tmp_end > end_time:
                result[i] += (end_time - tmp_start)
            elif tmp_start <= start_time and tmp_end >= end_time:
                result[i] += (end_time - start_time)
            elif tmp_start <= start_time and start_time <= tmp_end <= end_time:
                result[i] += (tmp_end - start_time)
        if result[i] > res:
            res = result[i]
            answer = start_time
    print(result)
    return m_time(answer)


logs = ["01:20:15-01:45:14", "00:40:31-01:00:00",
        "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]
adv_time = "00:14:15"
play_time = "02:03:55"

logs = ["69:59:59-89:59:59", "01:00:00-21:00:00",
        "79:59:59-99:59:59", "11:00:00-31:00:00"]
adv_time = "25:00:00"
play_time = "99:59:59"
print(solution(play_time, adv_time, logs))
