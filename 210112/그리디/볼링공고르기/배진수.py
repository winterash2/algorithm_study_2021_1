from itertools import combinations

n, m = map(int, input().split())
balls = list(map(int, input().split()))

# 2개를 뽑는 조합 수 구하기
result = list(combinations(balls, 2))
count = 0
# 21.1.15 스터디 후 수정 remove()는 앞에서부터 먼저 있는 한개만 제거함. 전체를 삭제해야 하기 때문에 수정
# 중복되는 무게가 있다면 제거
# for i in range(1, m+1):
#     if balls.count(i) > 1:
#         result.remove((i,i))

for i in range(1,m+1):
    if balls.count(i) > 1:
        count += result.count((i,i))
# 갯수 출력      
print(len(result)-count)