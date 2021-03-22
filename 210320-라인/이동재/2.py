def solution(inp_str):
    answer = []
    upper = 0
    lower = 0
    num = 0
    spc = 0
    # 1번 조건
    if len(inp_str) < 8 or len(inp_str) > 15:
        answer.append(1)
    # 2번 조건
    for elem in inp_str:
        if elem.isalpha():
            if elem.isupper():
                upper += 1
            elif elem.islower():
                lower += 1
        elif elem.isdigit():
            num += 1
        elif elem == '~' or elem == '!' or elem == '@' or elem == '#' or elem == '$' or elem == '%' or elem == '^' or elem == '&' or elem == '*':
            spc += 1
        else:
            if 2 not in answer:
                answer.append(2)

    # 3번 조건
    count = 0
    if upper == 0:
        count += 1
    if lower == 0:
        count += 1
    if num == 0:
        count += 1
    if spc == 0:
        count += 1
    if count >= 2:
        answer.append(3)
    # 4번 조건
    temp = list(inp_str)
    prev = temp[0]
    count = 1
    for elem in temp[1:]:
        if elem == prev:
            count += 1
        else:
            count = 1
        if count >= 4:
            answer.append(4)
            break
        prev = elem
    # 5번 조건
    temp = list(inp_str)
    temp.sort()
    prev = temp[0]
    count = 1
    for elem in temp[1:]:
        if elem == prev:
            count += 1
        else:
            count = 1
        if count >= 5:
            answer.append(5)
            break
        prev = elem
    if not answer:
        answer.append(0)

    return answer


# print(solution("CaCbCgCdC888834A"))
# print(solution("aaaaZZZZ)"))
print(solution("AaTa+!12-3"))
# print(solution("ZzZz9Z824"))


# 8 ≤ password 길이 ≤ 15
# password는 아래 4 종류의 문자 그룹을 제외한, 다른 어떤 문자도 포함해서는 안됩니다.
# [1] 알파벳 대문자(A~Z)
# [2] 알파벳 소문자(a~z)
# [3] 숫자(0~9)
# [4] 특수문자(~!@#$%^&*)
# password는 (2.)에서 명시된 4 종류의 문자 그룹 중에서 3 종류 이상을 포함해야 합니다.
# password에 같은 문자가 4개 이상 연속될 수 없습니다.
# password에 같은 문자가 5개 이상 포함될 수 없습니다.
