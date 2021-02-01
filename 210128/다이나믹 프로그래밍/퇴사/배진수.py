n = int(input())
work = []
for _ in range(n):
    days, money = map(int, input().split())
    work.append([days, money])

for i in range(0, n):
    if work[i][0] + i > n:
        work[i][1] = 0

for i in range(0, n):
    day = i
    res = 0
    while day < n:
        res += work[day][1]
        day += work[day][0]
    work[i][1] = res
    
work.sort(key=lambda x:x[1])
# print(work)
print(work[-1][1])