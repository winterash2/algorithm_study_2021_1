A = input()
B = input()

list_a = []
list_b = []

for a in A:
    list_a.append(a)
for b in B:
    list_b.append(b)

count = 0

# 길이가 다를 때
if len(list_a) != len(list_b):
    diff = abs(len(list_a) - len(list_b))
    # 다른 길이 만큼 짧은 쪽에 0을 넣어주고 두 문자열이 같아질때까지 비교 후 총 결과 값에 diff * 2 만큼 빼줌(0을 넣기때문에 다르고, 원래는 그 위치에 맞게 들어가기 때문)
    if len(list_a) < len(list_b):
        for _ in range(diff):
            list_a.append(0)
        for i in range(len(list_b)):
            if list_a[i] != list_b[i]:
                count += 1
                if i != len(list_b):
                    temp = list_a[i+1:]
                    list_a[i] = list_b[i]
                    list_a = list_a[:i+1] + temp
                else:
                    list_a.append(list_b[i])
    else:
        for _ in range(diff):
            list_b.append(0)
        for i in range(len(list_a)):
            if list_a[i] != list_b[i]:
                count += 1
                if i != len(list_a):
                    temp = list_a[i+1:]
                    list_a = list_a[:i] + temp
                else:
                    list_a = list_a[:i]
    count -= (diff * 2)
# 길이가 같을 때
else:
    for i in range(len(list_b)):
        if list_a[i] != list_b[i]:
            count += 1
            if i != len(list_b):
                temp = list_a[i+1:]
                list_a[i] = list_b[i]
                list_a = list_a[:i+1] + temp
            else:
                list_a.append(list_b[i])

# print(list_a, list_b)
print(count)