# target: 손님이 원하는 떡의 길이, start: 0, end: 제일 긴 떡의 길이
def cut(rice_cake, target, start, end):
    global max_result
    
    total = 0
    if start > end:
        return max_result
    mid = (start + end) // 2
    
    for i in rice_cake:
        if mid > i:
            continue
        total += (i - mid)
        
    
    # if total == target:
    #     return mid
    # max_result가 mid값을 가지고 있기 때문에 지워도댐 
    if total >= target:
        max_result = mid  # 여기선 max비교 안해도 됨.
        return cut(rice_cake, target, mid + 1, end)
    else:
        return cut(rice_cake, target, start, mid - 1)
    

# n, m = map(int, input().split())
n, m = 4, 6
# rice_cake = list(map(int, input().split()))
rice_cake = [19, 15, 10, 17]
rice_cake.sort()
max_length = max(rice_cake)
max_result = 0
result = cut(rice_cake, m, 0, max_length)
print(result)

