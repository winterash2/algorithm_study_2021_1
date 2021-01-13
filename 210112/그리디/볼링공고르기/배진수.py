from itertools import combinations

n, m = map(int, input().split())
balls = list(map(int, input().split()))

# 2개를 뽑는 조합 수 구하기
result = list(combinations(balls, 2))

# 중복되는 무게가 있다면 제거
for i in range(1, m+1):
    if balls.count(i) > 1:
        result.remove((i,i))
# 갯수 출력      
print(len(result))