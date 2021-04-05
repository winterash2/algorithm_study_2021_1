def distribute(parent_dict, money_dict, person, money):
    not_my = money // 10
    my = money - not_my
    my = my + money_dict[person]
    money_dict[person] = my
    if parent_dict[person] != '-' and not_my != 0:
        distribute(parent_dict, money_dict, parent_dict[person], not_my)


def solution(enroll, referral, seller, amount):
    answer = []
    parent_dict = dict()
    money_dict = dict()
    
    for i in range(len(enroll)):
        parent_dict[enroll[i]] = referral[i]
        money_dict[enroll[i]] = 0
    
    for i in range(len(seller)):
        person = seller[i]
        money = amount[i] * 100
        distribute(parent_dict, money_dict, person, money)
    
    for person in enroll:
        answer.append(money_dict[person])

    return answer


enroll = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
referral = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
seller = ["young", "john", "tod", "emily", "mary"]
amount = [12, 4, 2, 5, 10]
print(solution(enroll, referral, seller, amount))