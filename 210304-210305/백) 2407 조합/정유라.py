# http://boj.kr/2407
import math

# nCm = nPm / m! = n! / m!(n-m)!
n, m = map(int, input().split())
up = math.factorial(n)
down = (math.factorial(n-m)) * (math.factorial(m))
print(up // down)