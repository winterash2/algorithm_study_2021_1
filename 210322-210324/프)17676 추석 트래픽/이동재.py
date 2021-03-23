from bisect import bisect_left

def solution(lines):
    lines_orig = [x for x in lines]
    answer = 0
    lines = []

    for line in lines_orig:
        _, start, dur = line.split()
        hh, mm, ss = start.split(":")
        hh, mm = map(int, [hh, mm])
        ss, sss = map(int, ss.split("."))
        dur = dur[:-1].split(".")
        ss_dur = int(dur[0])
        if len(dur) == 2:
            sss_dur = int(dur[1])
        else:
            sss_dur = 0

        hh_end = hh
        mm_end = mm
        ss_end = ss + 1
        sss_end = sss - 1
        if sss_end < 0:
            sss_end += 1000
            ss_end -= 1
        if ss_end >= 60:
            ss_end -= 60
            mm_end += 1
            if mm_end >= 60:
                mm_end -= 60
                hh_end += 1
        end = (hh_end, mm_end, ss_end, sss_end)

        sss -= (sss_dur - 1)
        if sss < 0:
            sss += 1000
            ss -= 1
        ss -= ss_dur
        if ss < 0:
            ss += 60
            mm -= 1
        if mm < 0:
            mm += 60
            hh -= 1

        start = (hh, mm, ss, sss)
        lines.append((start, end))

    lines.sort()

    stack = []
    count = 0
    for line in lines:
        start, end = line
        while stack and stack[0] < start:
            stack = stack[1:]
            count -= 1
        stack.insert(bisect_left(stack, end), end)
        count += 1
        answer = max(answer, count)

    return answer


lines = ['2016-09-15 20:59:57.421 0.351s', '2016-09-15 20:59:58.233 1.181s', '2016-09-15 20:59:58.299 0.8s', '2016-09-15 20:59:58.688 1.041s', '2016-09-15 20:59:59.591 1.412s',
         '2016-09-15 21:00:00.464 1.466s', '2016-09-15 21:00:00.741 1.581s', '2016-09-15 21:00:00.748 2.31s', '2016-09-15 21:00:00.966 0.381s', '2016-09-15 21:00:02.066 2.62s']
lines = [
    "2016-09-15 01:00:04.002 2.0s",
    "2016-09-15 01:00:07.000 2s"
]
print(solution(lines))


# 시작시간, 기간 이렇게 들어오는 줄 알았음
"""
from collections import deque

def solution(lines):
    lines_orig = [x for x in lines]
    answer = 0
    lines = []

    for line in lines_orig:
        _, start, dur = line.split()
        hh, mm, ss = start.split(":")
        hh, mm = map(int, [hh, mm])
        ss, sss = map(int, ss.split("."))
        dur = dur[:-1].split(".")
        ss_dur = int(dur[0])
        if len(dur) == 2:
            sss_dur = int(dur[1])
        else:
            sss_dur = 0

        start = (hh, mm, ss, sss)

        sss = sss + sss_dur
        if sss >= 1000:
            sss -= 1000
            ss += 1
        ss = ss + ss_dur
        if ss >= 60:
            ss -= 60
            mm += 1
        if mm >= 60:
            mm -= 60
            hh += 1

        end = (hh, mm, ss, sss)
        lines.append((start, end))

    stack = deque()
    count = 0
    for line in lines:
        start, end = line
        while stack and stack[0][1] < start:
            stack.popleft()
            count -= 1
        stack.append(line)
        count += 1
        answer = max(answer, count)

    return answer
"""
