def solution(enter, leave):
    answer = []
    count_set = [set() for _ in range(len(enter)+1)]
    room = []
    
    leave_idx = 0
    for elem in enter:
        while leave[leave_idx] in room:
            leave_person = leave[leave_idx]
            room.remove(leave[leave_idx])
            leave_idx += 1
            # print(room)
            for person in room:
                count_set[person].add(leave_person)
                count_set[leave_person].add(person)
        for person in room:
            count_set[person].add(elem)
            count_set[elem].add(person)
        room.append(elem)
        # print(room)

    for i in range(1, len(enter)+1):
        answer.append(len(count_set[i]))
    # print(count_set)
    
    return answer

enter = [1,4,2,3]
leave = [2,1,3,4]
print(solution(enter, leave))

# [0, 1, 3, 4, 2]
# [0, 2, 1, 3, 4]












# 바보같이 푼 것
"""
def solution(enter, leave):
    answer = []


    enter_idx = [0 for _ in range(len(enter)+1)]
    leave_idx = [0 for _ in range(len(enter)+1)]
    for i in range(len(enter)):
        enter_idx[enter[i]] = i + 1
        leave_idx[leave[i]] = i + 1
    
    for i in range(1, len(enter)+1):
        count = 0
        print("i", i)
        for j in range(1, len(enter)+1):
            # 먼저 들어왔는데 더 늦게 나가는 경우
            if enter_idx[j] < enter_idx[i] and leave_idx[j] > leave_idx[i]:
                print("j1", j)
                count += 1
            # 나중에 들어왔는데 더 일찍 나가는 경우
            elif enter_idx[j] > enter_idx[i] and leave_idx[j] < leave_idx[i]:
                print("j2", j)
                count += 1
        answer.append(count)
    
    return answer
"""