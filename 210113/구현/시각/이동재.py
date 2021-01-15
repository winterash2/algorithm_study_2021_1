n = int(input())

# 아주 바보같이 푼 것
"""
number_get_3 = [3, 13, 23, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 43, 53]
check_hour = 0
check_minute = 0
check_second = 0
count = 0
for hour in range(n+1):
    if hour in number_get_3:
        check_hour = 1
    else:
        check_hour = 0
    for minute in range(60):
        if minute in number_get_3:
            check_minute = 1
        else:
            check_minute = 0
        for second in range(60):
            if second in number_get_3:
                check_second = 1
            else:
                check_second = 0
            if (check_hour + check_minute + check_second) > 0:
                count += 1

print(count)
"""

count = 0
for hour in range(n+1):
    for minute in range(60):
        for second in range(60):
            if '3' in str(hour)+str(minute)+str(second):
                count += 1

print(count)
