n = int(input())
arr = [int(i) for i in input().split()]
arr.sort()

# 최종 팀
total_team = 0

# 한 팀으로 묶일 팀원들 세기위함
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