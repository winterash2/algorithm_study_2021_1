import sys
# import operator
input = sys.stdin.readline

# 학생 수
N=int(input())

arr=[]

for i in range(N):
    [name, kor, eng, math] = map(str, input().split())
    arr.append([name, int(kor), int(eng), int(math)])
sorted_arr = sorted(arr, key=lambda x : (-x[1], x[2], -x[3], x[0]))
    
for score in sorted_arr:
    print(score[0])









# 실험
# for i in range(N):
#     M=input().split()
#     K=dict()
#     K['name']=M[0]
#     K['ko']=int(M[1])
#     K['en']=int(M[2])
#     K['math']=int(M[3])
#     arr.append(K)

# # print(arr)
# # sorted_arr=sorted(arr, key=operator.itemgetter('ko'), reverse=True)
# # sorted_arr=sorted(arr, key=operator.itemgetter('en'))
# # sorted_arr=sorted(arr, key=operator.itemgetter('math'), reverse=True)
# # sorted_arr=sorted(arr, key=operator.itemgetter('name'))

# print(sorted_arr, type(sorted_arr))

# # for a in sorted_arr:
# #     print(a[0],end=' ')


