# 왼쪽에서부터 봤을 때 최소값이랑
# 오른쪽에서부터 봤을 때 최소값을 구해둔 dp 테이블 두 개를 이용
def solution(a):
    answer = 2 # 맨 왼쪽, 맨 오른쪽은 무조건 됨
    minLeft = []
    minValue = 1e9
    for elem in a:
        if elem < minValue:
            minValue = elem
        minLeft.append(minValue)
    minRight = []
    minValue = 1e9
    for elem in a[::-1]:
        if elem < minValue:
            minValue = elem
        minRight.append(minValue)
    minRight = minRight[::-1]
    
    for idx in range(1, len(a)-1):
        if minLeft[idx-1] < a[idx] and minRight[idx+1] < a[idx]:
            pass
        else:
            answer += 1

    return answer

a = [-16,27,65,-2,58,-92,-71,-68,-61,-33]
print(solution(a))
# 정확성  테스트
# 테스트 1 〉	통과 (0.01ms, 10.2MB)
# 테스트 2 〉	통과 (0.01ms, 10.2MB)
# 테스트 3 〉	통과 (0.49ms, 10.2MB)
# 테스트 4 〉	통과 (33.13ms, 16.8MB)
# 테스트 5 〉	통과 (162.98ms, 44.4MB)
# 테스트 6 〉	통과 (241.37ms, 59.6MB)
# 테스트 7 〉	통과 (325.96ms, 76.8MB)
# 테스트 8 〉	통과 (321.86ms, 76.6MB)
# 테스트 9 〉	통과 (333.69ms, 76.7MB)
# 테스트 10 〉	통과 (325.16ms, 76.7MB)
# 테스트 11 〉	통과 (297.88ms, 76.8MB)
# 테스트 12 〉	통과 (307.40ms, 76.6MB)
# 테스트 13 〉	통과 (322.28ms, 76.8MB)
# 테스트 14 〉	통과 (295.02ms, 76.5MB)
# 테스트 15 〉	통과 (295.06ms, 76.8MB)


# 배열을 다 떼서 임시 배열을 만든 후에 일일히 처리
# 문제를 푸는 아이디어가 타당한지 확인은 한 것 같음
# 테스트 케이스 3개 통과하고 나머지는 다 시간초과
"""
def solution(a):
    answer = 2 # 맨 왼쪽, 맨 오른쪽은 무조건 됨
    for idx in range(1, len(a)-1):
        left = a[:idx]
        right = a[idx+1:]
        
        left = min(left)
        right = min(right)
        if left < a[idx] and right < a[idx]:
            pass
        else:
            answer += 1
        
    return answer
"""