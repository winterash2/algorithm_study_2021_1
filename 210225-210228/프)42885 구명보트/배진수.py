def solution(people, limit):
    answer = 0
    people.sort(reverse=True)
    i = 0
    j = len(people) - 1
    while i <= j:
        if people[i] <= (limit // 2):
            if (j - i + 1) % 2 == 0:
                answer += ((j - i + 1) // 2)
                break
            else:
                answer += (((j - i + 1) // 2) + 1)
                break
        else:
            if people[i] + people[j] <= limit:
                answer += 1
                i += 1
                j -= 1
            else:
                answer += 1
                i += 1
    return answer



people = [70, 80, 50]
limit = 100
print(solution(people, limit))

"""
정확성  테스트
테스트 1 〉	통과 (1.38ms, 10.3MB)
테스트 2 〉	통과 (1.26ms, 10.3MB)
테스트 3 〉	통과 (1.09ms, 10.3MB)
테스트 4 〉	통과 (1.02ms, 10.3MB)
테스트 5 〉	통과 (0.61ms, 10.2MB)
테스트 6 〉	통과 (0.34ms, 10.2MB)
테스트 7 〉	통과 (0.54ms, 10.2MB)
테스트 8 〉	통과 (0.05ms, 10.1MB)
테스트 9 〉	통과 (0.08ms, 10.2MB)
테스트 10 〉통과 (1.08ms, 10.1MB)
테스트 11 〉통과 (0.88ms, 10.2MB)
테스트 12 〉통과 (0.82ms, 10.2MB)
테스트 13 〉통과 (1.08ms, 10.3MB)
테스트 14 〉통과 (1.29ms, 10.2MB)
테스트 15 〉통과 (0.12ms, 10.2MB)
효율성  테스트
테스트 1 〉	통과 (10.13ms, 10.5MB)
테스트 2 〉	통과 (12.03ms, 10.5MB)
테스트 3 〉	통과 (10.31ms, 10.6MB)
테스트 4 〉	통과 (12.01ms, 10.6MB)
테스트 5 〉	통과 (10.82ms, 10.6MB)
"""