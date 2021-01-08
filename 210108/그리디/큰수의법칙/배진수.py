# 수가 커지게되면 시간초과 나는 방법
# N, M, K = map(int, input().split())
# num_list = list(map(int, input().split()))

# result = 0
# temp = 0
# num_list.sort()
# first = num_list[N-1]
# second = num_list[N-2]

# while M>0:
#     if temp != K:
#         result += first
#         temp+=1
#         M-=1
#     else:
#         temp = 0
#         result += second
#         M-=1
# print(result)

N, M, K = map(int, input().split())
num_list = list(map(int, input().split()))

num_list.sort()
first = num_list[N-1]
second = num_list[N-2]

# 가장 큰 수가 더해지는 횟수
count = int(M / (K+1)) * k
count += M % (K+1)

result = 0
result += count * first
result += (M-count) * second

print(result)