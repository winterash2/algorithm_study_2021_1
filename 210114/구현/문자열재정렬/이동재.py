# input_str = input()
input_str = "K1KA5CB7"
# input_str = "AJKDLSI412K4JSJ9D"

char_list = []
input_sum = 0
for i in input_str:
    if i.isdigit():
        input_sum += int(i)
    else:
        char_list.append(i)

char_list.sort()

# 유라꺼 참고해서 아래껄로 바꿈
# result = ""
# for char in char_list:
#     result += char
# result += str(input_sum)
# print(result)

result = "".join(char_list)+str(input_sum)
print(result)
