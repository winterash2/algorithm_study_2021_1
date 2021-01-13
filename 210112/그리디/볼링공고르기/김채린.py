n, m = map(int, input().split())
weight=list(map(int,input().split()))


# nC2
def com(num):
    all_num=(num*(num-1))//2
    return all_num

total=com(n)

#  중복제거
set_weight=set(weight)

for i in set_weight:
    print(i, weight.count(i))
    a=weight.count(i)
    if a!=1:
        print(com(a))
        total=total-com(a)
    
print(total)