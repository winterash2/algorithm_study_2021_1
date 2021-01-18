n=6
k=3
apple_pos=[(3,4), (2,5), (5,3)]
l=3
l_num=[[3,'D'],[15,'L'],[17,'D']]
# D는+1 이고 L= -1....

head_pos=[1,1]
look=0
road=[0,1,2,3]
# 보는 방향을..동서남북

count=0
result=0

for i in range(0,l):

    
    if l_num[i][0]>n-head_pos[0]:
        result= count+n-head_pos[0]


    head_pos[0]+=1
    head_pos[1]+=1
    