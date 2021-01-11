s = input()

make_1 = 0
make_0 = 0

list_1 = []
list_0 = []

# 1로 만들때 횟수 구하기
for i in range(len(s)):
    if i == 0:
        list_1.append(int(s[i]))
    else:
        if int(s[i-1]) != int(s[i]):
            list_1.append(int(s[i]))
for num in list_1:
    if num == 0:
        make_1 += 1
# 0으로 반들때 횟수 구하기
for i in range(len(s)):
    if i == 0:
        list_0.append(int(s[i]))
    else:
        if int(s[i-1]) != int(s[i]):
            list_0.append(int(s[i]))
for num in list_0:
    if num == 1:
        make_0 += 1
# 둘중 최소값 출력
print(min(make_0, make_1))