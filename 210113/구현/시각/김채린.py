
n = int(input())
count = 0

for h in range(n+1):    
    for m in range(60):
        for s in range(60):
            if '3' in str(h) +str(m)+str(s):
                count += 1

print(count)

#굳이 공식만들어보겠다고 뻘짓_..애잉 쯧ㅋㅋ

# n= int(input())

# non_three_h=(15*9+60)*5+600
# result=0

# if n<3:
#     result=non_three_h*(n+1)
# elif 3<=n<13:
#     result=non_three_h*(n)+3600
# elif 13<=n<23:
#     result=non_three_h*(n-1)+3600*2
# elif n==23:
#     result=non_three_h*(n-2)+3600*3
# else:
#     print('입력범위 초과')

# print(result)
