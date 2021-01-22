import itertools

#배운거 안써먹는 나쁜 뇌...메모리 똥망코드679392KB..

n=int(input())
a=list(map(int,input().split()))
m=list(map(int,input().split()))

arr_m=list('+'*m[0] + '-'*m[1] +'*'*m[2] +'/'*m[3])
nPr = list(itertools.permutations(arr_m, n-1))
cal_arr=list(set(nPr))

val_arr=[]

for cal in cal_arr:
    cal=list(cal)
    j=0
    result=a[j]
    for i in cal:
        if i=='/':
            if result<0:
                result=-(-result//a[j+1])
            else:
                result=(result//a[j+1])
        else:
            result=eval(str(result)+i+str(a[j+1]))
        j+=1
    val_arr.append(result)
    


print(max(val_arr))
print(min(val_arr))
