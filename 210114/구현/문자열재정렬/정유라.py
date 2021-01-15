alpha_list = list(input())
alpha_list.sort()
number_total = 0

for i in range(len(alpha_list)):
    # 알파벳이 시작되는 곳을 기준으로 리스트 slice
    if alpha_list[i].isalpha():
        alpha_list = alpha_list[i:len(alpha_list)]
        break

    # 알파벳이 시작되기 전까지 숫자들은 모두 더해주기
    number_total += int(alpha_list[i])


result = ''.join(alpha_list)+str(number_total)
print(result)
