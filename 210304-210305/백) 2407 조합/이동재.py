n, m = map(int, input().split())


def factorial(n):
    answer = 1
    while n:
        answer *= n
        n -= 1
    return answer


nCr = factorial(n) // (factorial(n-m) * factorial(m))
print(nCr)
