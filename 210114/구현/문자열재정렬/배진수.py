s = input()

str_data = []
int_data = []

# print(ord('A'), ord('Z'))
for data in s:
    # 알파벳이면 str에 append
    if 65 <= ord(data) <= 90:
        str_data.append(data)
    else: # 숫자면 int에 append
        int_data.append(data)

result = str_data + int_data
# 두 배열 합친 후 리스트를 문자열로 변환 후 출력
print(''.join(result))