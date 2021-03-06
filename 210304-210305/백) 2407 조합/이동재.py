# math 라이브러리에서 팩토리얼 임포트해서 쓰면 시간 쪼금 더 걸림
# 구현했을때는 64ms, 가져다 쓰면 68ms
from math import factorial

n, m = map(int, input().split())
nCr = factorial(n) // (factorial(n-m) * factorial(m))
print(nCr)

"""
n, m = map(int, input().split())


def factorial(n):
    answer = 1
    while n:
        answer *= n
        n -= 1
    return answer


nCr = factorial(n) // (factorial(n-m) * factorial(m))
print(nCr)
"""