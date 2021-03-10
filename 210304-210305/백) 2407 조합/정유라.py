# http://boj.kr/2407
import math

# nCm = nPm / m! = n! / m!(n-m)!
n, m = map(int, input().split())
up = math.factorial(n)
down = (math.factorial(n-m)) * (math.factorial(m))
print(up // down)

# def fac(i):
#     result = 1
#     while i > 1:
#         result *= i
#         i -= 1
#     return result

# up = fac(n)
# down = (fac(n-m)) * (fac(m))
# print(up // down)