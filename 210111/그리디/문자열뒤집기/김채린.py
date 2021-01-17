n=input()
change_list=list(map(int, n))

arr=[]
for i in range(0, len(change_list)-1):
    if change_list[i]==change_list[i+1]:
        continue
    else:
        arr.append(i+1)
    
if len(arr)%2==0:
    result=len(arr)//2
else:
    result=len(arr)//2+1

print(result)

