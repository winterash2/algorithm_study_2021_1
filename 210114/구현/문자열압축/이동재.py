def solution(s):
    input_str = s
    max_len = len(input_str)

    result = max_len
    for i in range(1, max_len//2+1):
        # print("-"*30)
        # i개만큼 문자열을 잘라서 리스트에 append
        temp_str = input_str
        sliced_list = []
        while True:
            sliced_list.append(temp_str[:i])
            temp_str = temp_str[i:]
            if temp_str == "":
                break
        # print(sliced_list)
        # 잘라진 문자열을 반복문을 돌면서 이전꺼랑 같은지 확인, 같으면 이전꺼를 ""공백문자로 수정
        # 이전꺼랑 같으면 넘어가고 아닌게 나오면 전전꺼를 그 개수로 수정
        prev = sliced_list[0]
        sliced_list.append("") # 마지막 요소까지 정확히 동작하게 하려고 그 어떤 문자와도 동일하지 않으면서 문자열을 합칠 때 없어지는 공백문자를 넣었음
        count = 0
        for i in range(1, len(sliced_list)):
            if sliced_list[i] == prev:
                count += 1
                sliced_list[i-1] = ""
            else:
                if count != 0:
                    sliced_list[i-2] = str(count+1)
                    count = 0
            prev = sliced_list[i]
            # print(sliced_list)
        # 숫자를 확인해서 같은거는 숫자로 바꾼 sliced_list를 문자열로 전부 붙이면 중간에 ""공백은 사라지기 때문에 정확한 문자열의 길이를 확인할 수 있음
        result_str = "".join(sliced_list)
        if result > len(result_str):
            result = len(result_str)
    answer = result
    return answer

# input_str = input()
# input_str = "xababcdcdababcdcd"
input_str = "abcabcabcabcdededededede"

print("aabbaccc"," 정답=", solution("aabbaccc"))
print("ababcdcdababcdcd"," 정답=", solution("ababcdcdababcdcd"))
print("abcabcdede"," 정답=", solution("abcabcdede"))
print("abcabcabcabcdededededede"," 정답=", solution("abcabcabcabcdededededede"))
print("xababcdcdababcdcd"," 정답=", solution("xababcdcdababcdcd"))