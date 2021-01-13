n = int(input())
data = [int(x) for x in input().split()]

data.sort()

num = 1
for d in data:
    if num < d:
        break
    num += d

print(num)

# https://www.acmicpc.net/problem/2437
# 채린 - 틀림
# 진수 - 메모리 초과
# 준의 - 자바라 못해봄
# 유라 - 맞음