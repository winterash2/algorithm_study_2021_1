n, m = map(int, input().split())    
data = list(map(int, input().split()))

# 중복되는 무게 제거
set_data = set(data)

same_weight = len(data) - len(set_data)
combination = n*(n-1)//2 - same_weight

print(combination)