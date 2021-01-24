n = int(input())

stages = list(map(int, input().split()))
stages.sort()
# 모든 스테이지 깨는 경우 때문에 n+2 해조야댐
count = [0] * (n + 2)
# count 인덱스가 stage 레벨 값, 배열 원소가 개수
for i in range(len(stages)):
    count[stages[i]] += 1

# fail에 stage값과 해당 stage값의 count값 튜플로 저장
fail = []
length = len(stages)

for i in range(1, len(count)-1):
    # 도전자 체크 다 했으면 남은 스테이지는 실패율 0으로 넣기
    if length == 0:
        fail.append((0,i))
    else:
        fail.append((count[i] / length, i))
        length -= count[i]
        
fail.sort(key=lambda x:(-x[0], x[1]))
result = [x[1] for x in fail]

print(result)