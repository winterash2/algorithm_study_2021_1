# https://www.acmicpc.net/problem/2110

# 도현이는 부자네..




n, c = 5, 3
houses = [1, 2, 8, 4, 9]
# house_point = []
# for _ in range(n):
#     house_point.append(int(input()))
# print(house_point)
houses.sort()


# 갓동빈 어찌된거애오..
# 동재코드 참고링 
start = 1 
end = (houses[-1] - houses[0]) // (c-1) + 1
print(start, end)
# sort후 houses
# 2, 5, 6, 8, 9
# start = 5-2 = 3
# end = 9-2 = 7


while (start <= end):
    count = 1
    value = houses[0]

    mid = (start + end) // 2  # 가장 인접한 두 공유기 사이의 거리 

    # 앞에서부터 차근차근 설치
    for i in range(1, n):
        if houses[i] >= value + mid:
            value = houses[i]
            count += 1
    
    # c개 이상 설치 할 수 있으면 거리 증가
    if count >= c:
        result = mid  # 최적의 결과 저장해두기
        start = mid + 1

    # 못하면 거리 감소
    else: 
        end = mid - 1

    

print(result)