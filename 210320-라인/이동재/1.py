def solution(table, languages, preference):
    answer = ''
    languages_dict = dict()
    for i in range(len(preference)):
        languages_dict[languages[i]] = preference[i]
    print(languages_dict)

    scoreM = 0
    for line in table:
        score = 0
        name, a, b, c, d, e = line.split()
        # 점수 계산
        if a in languages_dict:
            score += languages_dict[a] * 5
        if b in languages_dict:
            score += languages_dict[b] * 4
        if c in languages_dict:
            score += languages_dict[c] * 3
        if d in languages_dict:
            score += languages_dict[d] * 2
        if e in languages_dict:
            score += languages_dict[e] * 1
        if scoreM < score:
            scoreM = score
            answer = name
        
        if scoreM == score:
            answer_list = [answer]
            answer_list.append(name)
            answer_list.sort()
            answer = answer_list[0]

    return answer


table = ["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++",
         "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"]
languages = ["PYTHON", "C++", "SQL"]
preference = [7, 5, 5]
print(solution(table, languages, preference))


# def solution(table, languages, preference):
#     answer = ''
#     lang = dict()
#     for i in range(len(preference)):
#         lang.update({languages[i]: preference[i]})

#     temp = 0
#     for res in table:
#         sum_res = 0
#         name, a, b, l3, l4, l5 = res.split()
#         if l1 in lang:
#             sum_res += lang[l1] * 5
#         if l2 in lang:
#             sum_res += lang[l2] * 4
#         if l3 in lang:
#             sum_res += lang[l3] * 3
#         if l4 in lang:
#             sum_res += lang[l4] * 2
#         if l5 in lang:
#             sum_res += lang[l5] * 1
#         if temp < sum_res:
#             temp = sum_res
#             answer = name
#         if temp == sum_res:
#             tmp = [answer]
#             tmp.append(name)
#             tmp.sort()
#             answer = tmp[0]

#     return answer
