n = int(input())
data = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

max_result = -1e9
min_result = 1e9


def dfs(x, now):
    global add, sub, mul, div, max_result, min_result
    if n == x:
        max_result = max(max_result, now)
        min_result = min(min_result, now)

    else:
        if add > 0:
            add -= 1
            dfs(x+1, now + data[x])
            add += 1
        if sub > 0:
            sub -= 1
            dfs(x+1, now - data[x])
            sub += 1
        if mul > 0:
            mul -= 1
            dfs(x+1, now * data[x])
            mul += 1
        if div > 0:
            div -= 1
            dfs(x+1, int(now / data[x]))
            div += 1


dfs(1, data[0])
print(max_result)
print(min_result)
