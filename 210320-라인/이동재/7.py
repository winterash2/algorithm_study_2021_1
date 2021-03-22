# is_valid_program_name(command, program)
# command와 프로그램 이름을 인자로 받아 프로그램 이름 확인하고 True, False를 반환
# 인자
# command: 처리가 되지 않은 command 문자열
# program: 프로그램의 이름
# 반환값
# True or False
def is_valid_program_name(command, program):
    return True if program == command.split()[0] else False


# convert_flag_rules_to_flag_rule_dict_and_alias_dict(flag_rules)
# flag_rules 배열을 인자로 받아 flag_rule과 alias에 처리되는 dict형태로 변환
# flag_rule_dict의 예: flag_rule_dict = {'s': 'STRING', 'n': 'NUMBER', 'e': 'NULL'}
# alias_dict의 예: alias_dict = {'n': 'num'}
# 인자
# flag_rules: 처리되지 않은 flag_rules 배열
# 반환값
# flag_rule_dict, alias_dict
def convert_flag_rules_to_flag_rule_dict_and_alias_dict(flag_rules):
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
    return flag_rule_dict, alias_dict


# convert_command_to_dict(command, alias_dict)
# command 문자열을 인자로 받아 dict형태로 변환시킴(예: {'num': ['100'], 's': ['hi'], 'e': []})
# 인자
# command: 처리가 되지 않은 command 문자열
# alias_dict: ALIAS되는 flag_name을 처리하기 위한 {'flag_name_1': 'flag_name_2'} 형태의 dict
# 반환값
# 실패 시: False, 성공 시: command_dict
def convert_command_to_dict(command, alias_dict):
    command_list = command.split()
    command_dict = dict()
    is_valid = True
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
    if not is_valid:
        return is_valid
    else:
        return command_dict


# is_valid_command(flag_rule_dict, command_dict)
# command가 타당한지 확인함
# 인자
# flag_rule_dict: dict 형태로 변환된 flag_rule
# command_dict: dict 형태로 변환된 command
# 반환값
# True or False
def is_valid_command(flag_rule_dict, command_dict):
    is_valid = True
    # flag들의 validation을 확인
    for flag_name in command_dict.keys():
        # flag를 처리하는 룰이 없는 경우
        if flag_name not in flag_rule_dict.keys():
            is_valid = False
            break
        flag_argument_type = flag_rule_dict[flag_name]
        
        if flag_argument_type == 'NULL':
            # argument가 없는지 확인
            if command_dict[flag_name] != []:
                is_valid = False
                break
        elif flag_argument_type == 'NUMBER':
            # argument가 하나이고 숫자인지 확인
            if len(command_dict[flag_name]) != 1:
                is_valid = False
                break
            elif not command_dict[flag_name][0].isdigit():
                is_valid = False
                break
        elif flag_argument_type == 'NUMBERS':
            # argument가 한 개 이상인지 확인
            if len(command_dict[flag_name]) == 0:
                is_valid = False
                break
            # argument들이 숫자인지 확인
            for argument in command_dict[flag_name]:
                if not argument.isdigit():
                    is_valid = False
                    break
        elif flag_argument_type == 'STRING':
            # argument가 하나이고 알파벳으로만 이루어진 문자열인지 확인
            if len(command_dict[flag_name]) != 1:
                is_valid = False
                break
            for elem in command_dict[flag_name][0]:
                if not elem.isalpha():
                    is_valid = False
                    break
        elif flag_argument_type == 'STRINGS':
            # 인자가 한 개 이상인지 확인
            if len(command_dict[flag_name]) == 0:
                is_valid = False
                break
            # argument들이 알파벳으로만 이루어진 문자열인지 확인
            for argument in command_dict[flag_name]:
                for elem in argument:
                    if not elem.isalpha():
                        is_valid = False
                        break
    return is_valid


def solution(program, flag_rules, commands):
    answer = []
    for command in commands:
        is_valid = True
        # command를 공백 기준으로 분할
        command_list = command.split()

        # 프로그램 이름 확인
        is_valid = is_valid_program_name(command, program)

        # flag_rules 배열을 이용하여 flag_rule과 alias에 대한 dict형 자료 생성
        if is_valid:
            flag_rule_dict, alias_dict = convert_flag_rules_to_flag_rule_dict_and_alias_dict(flag_rules)

        # command를 flag_name:flag_argument[] 형태의 dict형 자료 생성
        # 예: {'n': ['100'], 's': ['hi'], 'e': []}
        if is_valid:
            command_dict = convert_command_to_dict(command, alias_dict)
            if command_dict == False:
                is_valid = False

        # command가 타당한지 확인
        if is_valid:
            is_valid = is_valid_command(flag_rule_dict, command_dict)
        
        # 검사 결과를 answer에 추가함
        answer.append(is_valid)

    return answer

program = "line"
flag_rules = ["-s STRING", "-num NUMBER", "-e NULL", "-n ALIAS -num"]
commands = ["line -n 100 -s hi -e", "line -n 100 -e -num 150"]
print(solution(program, flag_rules, commands))