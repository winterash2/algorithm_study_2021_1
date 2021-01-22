from collections import Counter

def solution(N, stages):
    stages.sort()

    counter = Counter(stages).most_common()
    counter.sort()

    size_stages = len(stages)
    result = []

    for i in range(1,N+1):
        result.append((i,0))

    for c in counter:
        if c[0] > N:
            break
        result.remove((c[0], 0))
        result.append((c[0], c[1]/size_stages))
        size_stages -= c[1]

    result.sort(key=lambda x: -x[1])
    fin = []
    for re in result:
        fin.append(re[0])
    return fin(re[0])
print(fin)

# 동재형 따라하기
# 테스트 1 〉	통과 (0.05ms, 10.2MB)
# 테스트 2 〉	통과 (0.20ms, 10.2MB)
# 테스트 3 〉	통과 (2.60ms, 10.6MB)
# 테스트 4 〉	통과 (14.50ms, 11.2MB)
# 테스트 5 〉	통과 (39.33ms, 15.6MB)
# 테스트 6 〉	통과 (0.31ms, 10.2MB)
# 테스트 7 〉	통과 (3.64ms, 10.3MB)
# 테스트 8 〉	통과 (14.51ms, 11.2MB)
# 테스트 9 〉	통과 (38.81ms, 15.7MB)
# 테스트 10 〉	통과 (12.91ms, 11.3MB)
# 테스트 11 〉	통과 (13.47ms, 11.2MB)
# 테스트 12 〉	통과 (18.41ms, 11.9MB)
# 테스트 13 〉	통과 (21.71ms, 12MB)
# 테스트 14 〉	통과 (0.06ms, 10.2MB)
# 테스트 15 〉	통과 (5.92ms, 10.6MB)
# 테스트 16 〉	통과 (3.42ms, 10.4MB)
# 테스트 17 〉	통과 (5.90ms, 10.6MB)
# 테스트 18 〉	통과 (3.12ms, 10.4MB)
# 테스트 19 〉	통과 (1.02ms, 10.2MB)
# 테스트 20 〉	통과 (4.96ms, 10.5MB)
# 테스트 21 〉	통과 (8.46ms, 11MB)
# 테스트 22 〉	통과 (14.88ms, 18.1MB)
# 테스트 23 〉	통과 (14.92ms, 12.1MB)
# 테스트 24 〉	통과 (21.64ms, 12.3MB)
# 테스트 25 〉	통과 (0.04ms, 10.2MB)
# 테스트 26 〉	통과 (0.05ms, 10.2MB)
# 테스트 27 〉	통과 (0.04ms, 10.2MB)