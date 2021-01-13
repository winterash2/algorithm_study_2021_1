n = int(input())
data = [int(x) for x in input().split()]

data.sort()

num = 1
for d in data:
    if num < d:
        break
    num += d

print(num)