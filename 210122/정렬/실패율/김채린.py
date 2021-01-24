import sys
input = sys.stdin.readline

def solution(N, stages):

    count=[0]*(N+2)
    rate=[]
    for i in range(len(stages)):
        count[stages[i]]+=1

    j=0
    for a in range(len(count)):
        if sum(count)-sum(count[0:a])==0:
            fail=0
        else:
            # 도달했으나 클리어 못한 수 / 스테이지에 도달한 플레이어의 수
            fail=count[a]/(sum(count)-sum(count[0:a]))
        rate.append([j,fail])
        j+=1

    rate=rate[1:N+1]
    sorted_rate = sorted(rate, key=lambda x : (-x[1]))

    answer=[]
    for k in sorted_rate:
        answer.append(k[0])
    return answer

# 그럼 나도 따라할래
# 테스트 1 〉	통과 (0.05ms, 10.2MB)
# 테스트 2 〉	통과 (0.16ms, 10.2MB)
# 테스트 3 〉	통과 (6.31ms, 10.5MB)
# 테스트 4 〉	통과 (9.96ms, 10.9MB)
# 테스트 5 〉	통과 (21.50ms, 15MB)
# 테스트 6 〉	통과 (0.49ms, 10.1MB)
# 테스트 7 〉	통과 (1.52ms, 10.2MB)
# 테스트 8 〉	통과 (11.34ms, 10.8MB)
# 테스트 9 〉	통과 (44.84ms, 14.9MB)
# 테스트 10 〉	통과 (9.27ms, 10.9MB)
# 테스트 11 〉	통과 (11.75ms, 10.9MB)
# 테스트 12 〉	통과 (13.71ms, 11.4MB)
# 테스트 13 〉	통과 (15.72ms, 11.4MB)
# 테스트 14 〉	통과 (0.07ms, 10.3MB)
# 테스트 15 〉	통과 (6.19ms, 10.6MB)
# 테스트 16 〉	통과 (3.46ms, 10.3MB)
# 테스트 17 〉	통과 (6.26ms, 10.6MB)
# 테스트 18 〉	통과 (3.41ms, 10.3MB)
# 테스트 19 〉	통과 (1.21ms, 10.4MB)
# 테스트 20 〉	통과 (6.14ms, 10.3MB)
# 테스트 21 〉	통과 (8.85ms, 10.9MB)
# 테스트 22 〉	통과 (22.67ms, 18MB)
# 테스트 23 〉	통과 (18.36ms, 11.7MB)
# 테스트 24 〉	통과 (18.01ms, 11.7MB)
# 테스트 25 〉	통과 (0.02ms, 10.2MB)
# 테스트 26 〉	통과 (0.02ms, 10.2MB)
# 테스트 27 〉	통과 (0.01ms, 10.2MB)