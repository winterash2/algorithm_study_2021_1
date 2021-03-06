n, r = map(int, input().split())

def factorial(x):
    res = 1
    while x != 1:
        res *= x
        x -= 1
    return res

result = (factorial(n)) // (factorial(n-r) * factorial(r))
print(result)