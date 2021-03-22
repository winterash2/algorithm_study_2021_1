# 프로그램 이름 확인
def is_valid_program_name(program, inp_str):
    return True if program == inp_str else False


def solution(program, flag_rules, commands):
    answer = []
    for command in commands:
        is_valid = True
        # command를 공백 기준으로 분할
        command_list = command.split()

        # 프로그램 이름 확인
        is_valid = is_valid_program_name(program, command_list[0])

        if is_valid:
            # flag_rules를 dict 형태로 변환, ALIAS를 처리할 때 사용되는 dict 생성
            # 예: flag_rule_dict = {'s': 'STRING', 'n': 'NUMBER', 'e': 'NULL'}
            # 예: alias_dict = {'n': 'num'}
            flag_rule_dict = dict()
            alias_dict = dict()
            for flag_rule in flag_rules:
                flag_rule_list = flag_rule.split()
                # ALIAS가 아닌 경우 flag_name과 flag_argument_type으로 길이가 2임
                if len(flag_rule_list) == 2:
                    flag_name, flag_argument_type = flag_rule.split()
                    flag_rule_dict[flag_name[1:]] = flag_argument_type
                # ALIAS인 경우 flag_name_1, ALIAS, flag_name_2로 길이가 3임
                elif len(flag_rule_list) == 3:
                    flag_name_1, _, flag_name_2 = flag_rule.split()
                    alias_dict[flag_name_1[1:]] = flag_name_2[1:]

        # command를 flag_name:flag_argument[] 형태의 dict로 변경
        # 예: {'n': ['100'], 's': ['hi'], 'e': []}
        if is_valid:
            command_dict = dict()
            i = 1
            while i < len(command_list):
                # -으로 시작하는 경우 flag_name혹은 ALIAS임
                if command_list[i][0] == '-':
                    key = command_list[i][1:]
                    # ALIAS인 경우 key를 본래 key로 변경
                    if key in alias_dict.keys():
                        key = alias_dict[key]
                    # 다음 flag_name이 올 때까지는 전부 flag_argument임
                    flag_argument_list = []
                    for j in range(i+1, len(command_list)):
                        if command_list[j][0] == '-':
                            break
                        else:
                            flag_argument_list.append(command_list[j])
                    # 이미 해당 flag_name에 대한 인자가 있는 경우 타당하지 않은 command임
                    if key in command_dict.keys():
                        is_valid = False
                        break
                    command_dict[key] = flag_argument_list
                    i += len(flag_argument_list)
                # flag_name이 없이 argument만 오는 경우
                else:
                    is_valid = False
                    break
                i += 1
        
        if is_valid:
            # flag들의 validation을 확인
            for flag_name in command_dict.keys():
                # flag를 처리하는 룰이 없는 경우
                if flag_name not in flag_rule_dict.keys():
                    is_valid = False
                    break
                # flag를 처리하는 룰이 있는 경우
                if flag_rule_dict[flag_name] == 'NULL':
                    # argument가 없는지 확인
                    if command_dict[flag_name] != []:
                        is_valid = False
                        break
                elif flag_rule_dict[flag_name] == 'NUMBER':
                    # argument가 하나이고 숫자인지 확인
                    if len(command_dict[flag_name]) != 1:
                        is_valid = False
                        break
                    elif not command_dict[flag_name][0].isdigit():
                        is_valid = False
                        break
                elif flag_rule_dict[flag_name] == 'NUMBERS':
                    # argument들이 숫자인지 확인
                    if len(command_dict[flag_name]) == 0:
                        is_valid = False
                        break
                    for argument in command_dict[flag_name]:
                        if not argument.isdigit():
                            is_valid = False
                            break
                elif flag_rule_dict[flag_name] == 'STRING':
                    # argument가 하나이고 알파벳으로만 이루어진 문자열인지 확인
                    if len(command_dict[flag_name]) != 1:
                        is_valid = False
                        break
                    for elem in command_dict[flag_name][0]:
                        if not elem.isalpha():
                            is_valid = False
                            break
                elif flag_rule_dict[flag_name] == 'STRINGS':
                    # argument들이 알파벳으로만 이루어진 문자열인지 확인
                    for argument in command_dict[flag_name]:
                        for elem in argument:
                            if not elem.isalpha():
                                is_valid = False
                                break
        answer.append(is_valid)

    return answer