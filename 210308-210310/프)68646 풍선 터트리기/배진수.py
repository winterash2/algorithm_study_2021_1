def solution(a):
    if len(a) == 1:
        return 1
    answer = len(a)
    left = a[0]
    right = min(a[1:])
    for i in range(1, len(a) - 1):
        if left > a[i]:
            left = a[i]
        if right == a[i]:
            right = min(a[i+1:])
        if left < a[i] and right < a[i]:
            answer -= 1
    return answer


a = [-16, 27, 65, -2, 58, -92, -71, -80, -68, -61, -180, -33]
print(solution(a))


"""
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.01ms, 10.2MB)
테스트 3 〉	통과 (0.39ms, 10.3MB)
테스트 4 〉	통과 (19.84ms, 14.5MB)
테스트 5 〉	통과 (100.07ms, 33.1MB)
테스트 6 〉	통과 (172.98ms, 44.7MB)
테스트 7 〉	통과 (198.47ms, 56.2MB)
테스트 8 〉	통과 (986.49ms, 56.1MB)
테스트 9 〉	통과 (3013.86ms, 56.2MB)
테스트 10 〉	실패 (시간 초과)
테스트 11 〉	실패 (시간 초과)
테스트 12 〉	실패 (시간 초과)
테스트 13 〉	실패 (시간 초과)
테스트 14 〉	실패 (시간 초과)
테스트 15 〉	실패 (시간 초과)
"""