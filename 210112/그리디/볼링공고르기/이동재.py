n, m = [int(x) for x in input().split()]
weight = [int(x) for x in input().split()]

weight.sort()

current = weight[0]
quantity = 0
result = 0
for w in weight:
    if w == current:
        quantity += 1
    else:
        result += (n * quantity)
        quantity = 1
        current = w
    n -= 1
print(result)
