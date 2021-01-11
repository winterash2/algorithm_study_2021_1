n = int(input())
data = [int(x) for x in input().split()]

data.sort()

party = 0
need = data[0]
get = 0

for i in data:
    if need == get:
        need = get = 0
        party += 1
    need = i
    get += 1

print(party)
