n, m = map(int, input().split())    
data = list(map(int, input().split()))
# 1, 3, 2, 3, 2
# (1, 3), (1, 2), (1, 3), (1, 2) -> 4
# (3, 2), (3, 3), (3, 2) -> 3
# (2, 3), (2, 2) -> 2
# (3, 2) -> 1

# 중복되는 무게 제거
set_data = set(data)

# 경우의 수 합 1부터 n까지의 합 n*(n+1)/2
same_weight = len(data) - len(set_data)
print("S", len(data), len(set_data))
combination = n*(n-1)//2 - same_weight

print(combination)