total = 0
isZero = False

arr = list(map(int, str(input())))

for i in arr:
    i = int(i)
    
    if i <= 1 or total <= 1:
        total += i
    else:
        total *= i
print(total)