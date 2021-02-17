def solution(name):
    answer = 0
    countList = []
    for n in name:
        countList.append(min(90 - ord(n) + 1, ord(n) - 65))
    idx = 0
    answer += countList[idx]
    countList[idx] = 0
    while countList.count(0) != len(name):
        # 이 부분 진수가 훨씬 간단하게 구현함. 아주 멋진 친구임
        for i in range(1, len(name)):
            if countList[idx - i] != 0:
                break
        left_count = i
        for i in range(1, len(name)):
            if countList[idx + i] != 0:
                break
        right_count = i

        if left_count < right_count:
            idx += left_count
            answer += left_count + countList[idx]
        else:
            idx += right_count
            answer += right_count + countList[idx]
        countList[idx] = 0
    
    return answer

print(solution("JEROEN"))
print(solution("JAN"))


"""
def solution(name):
    answer = 0
    # 각각의 요소가 A로부터 만들어지는데 필요한 조작의 수를 전부 계산
    for n in name:
        answer += min(90 - ord(n) + 1, ord(n) - 65)
    # name을 두 번 붙이고 (예: JEROENJEROEN) 한 칸씩 밀면서 len(name) 만큼 돌면서
    # A가 아닌거 다 탐색하는데 얼마나 걸리는지 셈
    minCount = 1e9
    for i in range(len(name)):
        namePart = (name + name)[i:i+len(name)]
        remainNotA = len(name) - name.count("A")
        count = min(i, len(name)-i)
        for n in namePart:
            if n != 'A':
                remainNotA -= 1
            if remainNotA == 0:
                break
            count += 1
        if count < minCount:
            minCount = count
    answer += minCount

    print(answer)
    return answer
"""