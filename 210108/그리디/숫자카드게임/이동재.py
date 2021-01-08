n, m = [int(x) for x in input().split()]

data = []

for i in range(n):
    data.append(min([int(x) for x in input().split()]))

print(max(data))
