total = 0
arr = list(map(str, input()))

for i in arr:
    i = int(i)
    # 숫자가 0 or 1 / 합계가 0 or 1인 경우 더하기
    if i <= 1 or total <= 1:
        total += i
    else:
        total *= i
print(total)