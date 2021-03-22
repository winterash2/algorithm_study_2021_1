# 프로그램 이름 확인
def is_valid_program_name(program, inp_str):
    return True if program == inp_str else False


def solution(program, flag_rules, commands):
    answer = []
    for command in commands:
        is_valid = True
        # command를 공백 기준으로 분할
        command_list = command.split()

        # flag_rules를 dict 형태로 변환 예: {'s': 'STRING', 'n': 'NUMBER', 'e': 'NULL'}
        flag_rules_dict = dict()
        for flag_rule in flag_rules:
            flag_name, flag_argument_type = flag_rule.split()
            flag_rules_dict[flag_name[1:]] = flag_argument_type
        print(flag_rules_dict)


        # 프로그램 이름 확인
        if not is_valid_program_name(program, command_list[0]):
            is_valid = False

        command_dict = dict()
        if is_valid:
            # command를 flag_name:flag_argument[] 형태의 dict로 변경
            # 예: {'n': ['100'], 's': ['hi'], 'e': []}
            i = 1
            while i < len(command_list):
                # flag_name으로 시작하는 경우
                if command_list[i][0] == '-':
                    key = command_list[i][1:]
                    values = []
                    for j in range(i+1, len(command_list)):
                        if command_list[j][0] == '-':
                            break
                        else:
                            values.append(command_list[j])
                    # 이미 해당 룰에 대한 인자가 들어온 경우 중복된 것이 들어왔기 때문에 타당하지 않음
                    if key in command_dict.keys():
                        is_valid = False
                        break
                    command_dict[key] = values
                    i += len(values)
                # flag_name이 없이 argument만 오는 경우
                else:
                    is_valid = False
                    break
                i += 1
        print(command_dict)
        
        if is_valid:
            # flag들의 validation을 확인
            for flag_name in command_dict.keys():
                # flag를 처리하는 룰이 없는 경우
                if flag_name not in flag_rules_dict.keys():
                    is_valid = False
                    break
                # flag를 처리하는 룰이 있는 경우
                if flag_rules_dict[flag_name] == 'NULL':
                    # argument가 없는지 확인
                    if command_dict[flag_name] != []:
                        is_valid = False
                        break
                elif flag_rules_dict[flag_name] == 'NUMBER':
                    # argument가 하나이고 숫자인지 확인
                    if len(command_dict[flag_name]) != 1:
                        is_valid = False
                        break
                    elif not command_dict[flag_name][0].isdigit():
                        is_valid = False
                        break
                elif flag_rules_dict[flag_name] == 'NUMBERS':
                    # argument들이 숫자인지 확인
                    if len(command_dict[flag_name]) == 0:
                        is_valid = False
                        break
                    for argument in command_dict[flag_name]:
                        if not argument.isdigit():
                            is_valid = False
                            break
                elif flag_rules_dict[flag_name] == 'STRING':
                    # argument가 하나이고 알파벳으로만 이루어진 문자열인지 확인
                    if len(command_dict[flag_name]) != 1:
                        is_valid = False
                        break
                    for elem in command_dict[flag_name][0]:
                        if not elem.isalpha():
                            is_valid = False
                            break
                elif flag_rules_dict[flag_name] == 'STRINGS':
                    # argument들이 알파벳으로만 이루어진 문자열인지 확인
                    for argument in command_dict[flag_name]:
                        for elem in argument:
                            if not elem.isalpha():
                                is_valid = False
                                break
        answer.append(is_valid)

    return answer

program = "trip"
flag_rules = ["-days NUMBERS", "-dest STRING"]
commands = ["trip -days 15 10 -dest Seoul Paris", "trip -days 10 -dest Seoul"]
print(solution(program, flag_rules, commands))
