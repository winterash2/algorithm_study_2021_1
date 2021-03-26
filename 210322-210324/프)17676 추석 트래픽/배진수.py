from datetime import datetime, timedelta


def solution(lines):
    answer = 0
    date_list = []
    for line in lines:
        y, t, need = line.split()
        need = float(need[:-1]) - 0.001
        date_time = y + ' ' + t
        time = datetime.strptime(date_time, '%Y-%m-%d %H:%M:%S.%f')
        date_list.append((time - timedelta(seconds=need), time))
    date_list.sort(key=lambda x: x[1])

    for x in date_list:
        start, end = x
        cnt1 = 0
        cnt2 = 0
        for y in date_list:
            ss, ee = y
            if start <= ss <= start + timedelta(seconds=0.999) or start <= ee <= start + timedelta(seconds=0.999):
                cnt1 += 1
            if end <= ss <= end + timedelta(seconds=0.999) or end <= ee <= end + timedelta(seconds=0.999):
                cnt2 += 1
            
        answer = max(answer, cnt1, cnt2)

    return answer


lines = [
    "2016-09-15 01:00:04.002 2.0s",
    "2016-09-15 01:00:07.000 2s"
]

lines = [
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
]

lines = ["2016-09-15 01:00:04.001 2.0s", "2016-09-15 01:00:07.000 2s"]
lines = ["2016-09-15 01:00:04.002 2.0s", "2016-09-15 01:00:07.000 2s"]
lines = ["2016-09-15 00:00:03.000 3s",
         "2016-09-15 00:00:03.000 2s", "2016-09-15 00:00:03.000 1s"]
print(solution(lines))

"""
실행 결과
채점을 시작합니다.
정확성  테스트
테스트 1 〉	통과 (2.85ms, 10.9MB)
테스트 2 〉	실패 (1098.25ms, 11.1MB)
테스트 3 〉	실패 (1019.33ms, 11.1MB)
테스트 4 〉	통과 (2.87ms, 10.8MB)
테스트 5 〉	통과 (13.87ms, 10.9MB)
테스트 6 〉	통과 (13.98ms, 11MB)
테스트 7 〉	통과 (1108.29ms, 11MB)
테스트 8 〉	통과 (1026.35ms, 11.1MB)
테스트 9 〉	통과 (14.20ms, 10.9MB)
테스트 10 〉통과 (2.94ms, 10.8MB)
테스트 11 〉통과 (3.08ms, 10.8MB)
테스트 12 〉통과 (1046.23ms, 11.1MB)
테스트 13 〉통과 (12.89ms, 10.8MB)
테스트 14 〉통과 (2.89ms, 10.9MB)
테스트 15 〉통과 (2.69ms, 10.9MB)
테스트 16 〉통과 (2.65ms, 10.8MB)
테스트 17 〉통과 (2.94ms, 10.9MB)
테스트 18 〉실패 (3669.57ms, 11.4MB)
테스트 19 〉통과 (4162.58ms, 11.4MB)
테스트 20 〉통과 (4112.08ms, 11.4MB)
테스트 21 〉통과 (2.75ms, 10.8MB)
테스트 22 〉통과 (2.58ms, 10.7MB)
채점 결과
정확성: 86.4
합계: 86.4 / 100.0
"""