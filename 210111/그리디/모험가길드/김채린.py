n=input()
fear_list=list(map(int,input().split()))
fear_list.sort()
print(fear_list)

count=0
idx=0
# 인원 조금 필요한 애부터 보내버리쥬~

while idx<=len(fear_list):
    if idx+fear_list[idx]<len(fear_list):
        idx+=fear_list[idx]
        count+=1
    else:
        break

print(count)
