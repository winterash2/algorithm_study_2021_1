score=int(input())
score=str(score)

mid_idx=int(len(score)/2)

left_arr=score[:mid_idx]
right_arr=score[mid_idx:]

left_num=0
right_num=0

for i in left_arr:
    left_num+=int(i)

for i in right_arr:
    right_num+=int(i)

if left_num==right_num:
    print("LUCKY")
else:
    print('READY')