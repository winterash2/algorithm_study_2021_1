n=input()
money=list(map(int,input().split()))
money.sort()
# 11239

# money_sum=sum(money)
a=1
money_sum=0
result=0

if 1 not in money:
    result=1
else:
    for i in money:
        if i>a:
            result=a
            break
        else:
            a+=i
print(result)

    