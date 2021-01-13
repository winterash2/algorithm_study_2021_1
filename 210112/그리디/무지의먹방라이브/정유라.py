# def solution(food_times, k):
    
#     index = len(food_times)
#     count = 0
#     while True:
#         i = count % index
#         if count == k+1:
#             answer = i+1
#             print(answer)
#             break
#         food_times[i] -= 1
#         count += 1
        
#     return answer

food_times = list(map(int, input().split()))
k = int(input())

index = len(food_times)
count = 0
print(index)
while count<10:
    i = count % index
    
    if count == k+1:
        print(i)
    food_times[i] -= 1
    count += 1
