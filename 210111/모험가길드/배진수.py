from collections import Counter

n = int(input())
fear_data = list(map(int, input().split()))

result = 0
count_data = Counter(fear_data).most_common()
count_data.sort()
print(count_data)

new_list = []
for data in count_data:
    new_list.append(list(data))

for i in range(len(new_list)-1):
    if new_list[i][1] >= new_list[i][0]:
        result += new_list[i][1] // new_list[i][0]
        new_list[i+1][1] += (new_list[i][1] % new_list[i][0])
    else:
        new_list[i+1][1] += new_list[i][1] % new_list[i][0]
if new_list[-1][1] >= new_list[-1][0]:
    result += new_list[-1][1] // new_list[-1][0]

print(result)

# 리스트에 있는 숫자를 중복된 값이 몇개 있는지 확인 
# 예제 -> [(1, 1), (2, 3), (3, 1)]
# 공포도가 1인 사람이 더 많다면 결과값에 몫을 더하고 나머지는 다음 공포도 사람수에 넘겨줌
