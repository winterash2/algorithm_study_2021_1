arr = list(map(int, str(input())))
# 0과 1 묶음 개수 센 뒤 적은 숫자를 뒤집는다
# 00001100 -> 0 묶음: 2개, 1 묶음: 1개 
total_zero = 0
total_one = 0
zero = 0
one = 0
for i in arr:
    if i == 0:
        if one != 0:
            total_one +=1
            one = 0
            zero += 1
        else:
            zero += 1
    elif i == 1:
        if zero != 0:
            total_zero += 1
            zero = 0
            one += 1
        else:
            one += 1

print(min(total_zero, total_one))

    
