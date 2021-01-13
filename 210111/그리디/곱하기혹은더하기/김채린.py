a=str(input())
arr=list(map(int, a))
print(a, arr)
result=0
for i in arr:
    if result==0 or result==1:
        result+=i
    elif i==0 or i==1:
        result+=i
    else:
        result*=i

print(result)