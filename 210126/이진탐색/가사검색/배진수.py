import re

def solution(words, queries):
    answer = []
    for query in queries:
        query = query.replace('?','.')
        count = 0
        for word in words:
            if re.findall(query, word) and len(query) == len(word):
                print(re.findall(query, word))
                count+=1
        answer.append(count)
    return answer

words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]
print(solution(words, queries))

##### 정규표현식으로 정확성은 맞음
### 효율성은 ....ㅜㅠㅠ
# 테스트 1 〉	통과 (2.65ms, 10.2MB)
# 테스트 2 〉	통과 (1.43ms, 10.2MB)
# 테스트 3 〉	통과 (1.67ms, 10.3MB)
# 테스트 4 〉	통과 (1.95ms, 10.2MB)
# 테스트 5 〉	통과 (2.03ms, 10.2MB)
# 테스트 6 〉	통과 (1.64ms, 10.2MB)
# 테스트 7 〉	통과 (40.18ms, 10.2MB)
# 테스트 8 〉	통과 (43.27ms, 10.2MB)
# 테스트 9 〉	통과 (55.96ms, 10.3MB)
# 테스트 10 〉	통과 (33.09ms, 10.3MB)
# 테스트 11 〉	통과 (29.62ms, 10.4MB)
# 테스트 12 〉	통과 (40.21ms, 10.3MB)
# 테스트 13 〉	통과 (672.87ms, 10.6MB)
# 테스트 14 〉	통과 (552.95ms, 10.6MB)
# 테스트 15 〉	통과 (665.07ms, 10.4MB)
# 테스트 16 〉	통과 (671.40ms, 10.4MB)
# 테스트 17 〉	통과 (542.13ms, 10.6MB)
# 테스트 18 〉	통과 (639.81ms, 10.6MB)

# 테스트 1 〉	실패 (시간 초과)
# 테스트 2 〉	실패 (시간 초과)
# 테스트 3 〉	실패 (시간 초과)
# 테스트 4 〉	실패 (시간 초과)
# 테스트 5 〉	통과 (1449.26ms, 21.9MB)