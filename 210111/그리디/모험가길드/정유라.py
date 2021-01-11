n = int(input())
arr = [int(i) for i in input().split()]
arr.sort()
total_team = 0
team = 0
count = 0
idx = 0

while True:
    
    count += 1
    if arr[idx] == count:
        count = 0
        total_team += 1
    idx += 1    
    if idx >= n:
        break

print(total_team)