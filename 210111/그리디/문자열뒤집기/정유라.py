 arr = list(map(int, str(input())))

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

    
