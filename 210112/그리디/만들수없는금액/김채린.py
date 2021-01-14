n=input()
money=list(map(int,input().split()))
money.sort()
# 11239

# money_sum=sum(money)
a=1

for i in money:
    if a<i:
        break
    else:
        a+=i
print(a)

    