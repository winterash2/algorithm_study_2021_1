# 틀렸음. 더 생각해봐야할듯.
def solution(food_times, k):
    answer = 0
    i=0
    idx=0

    if sum(food_times)<=k:
        answer=-1
    else:
        while idx!=k:
            if food_times[i]==0:
                if i==len(food_times)-1:
                    i=0
                else:
                    i+=1
            else:
                food_times[i]-=1
                idx+=1
                if i==len(food_times)-1:
                    i=0
                else:
                    i+=1
                answer=i+1
        
    return answer

print(solution([1,1,1], 3))