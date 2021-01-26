def count_x(array, x, start, end):
    global count
    
    if start > end:
        return count

    mid = (start + end) // 2
    # 중간 값이 x인 경우
    if array[mid] == x:
        count += 1

        # 좌, 우로 나눠서 찾기
        count_x(array, x, mid + 1, end)
        count_x(array, x, start, mid - 1)
        return count # 재귀 끝나고 오면 count 반환해주기
    elif array[mid] < x:
        return count_x(array, x, mid + 1, end)
    else:
        return count_x(array, x, start, mid - 1)

n, x = 7, 4
array = [1, 1, 2, 2, 2, 2, 3]
count = 0

result = count_x(array, x, 0, n-1)

if result == 0:
    print("-1")
else:
    print(result)