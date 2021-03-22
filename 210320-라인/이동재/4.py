def create_search_result(data_split, node):
    result = '' + node[1] + '/'
    # 부모 노드가 0이 아닌 경우
    if node[2] != 0:
        result = create_search_result(data_split, data_split[node[2]]) + result
    return result


def solution(data, word):
    answer = []
    l = len(word)
    data_split = [[]]
    for node in data:
        node_id, node_name, node_parent = node.split()
        node_id = int(node_id)
        node_parent = int(node_parent)
        data_split.append([node_id, node_name, node_parent])

    data_split.sort()
    # (이름, 결과 문자열) 리스트를 생성
    dolls = []
    for node in data_split[:1:-1]:
        node_id, node_name, node_parent = node
        # 현재 노드가 어떤 노드의 부모 노드인지 확인
        is_parent = False
        for i in range(1, len(data)+1):
            if data_split[i][2] == node_id:
                is_parent = True
                break
        # 현재 노드가 어떤 노드의 부모 노드이면 스킵
        if is_parent:
            continue
        # 현재 노드가 어떤 노드의 부모 노드가 아닌 경우
        result = create_search_result(data_split, node)
        dolls.append((node_name, node_id, result[:-1]))

    answer2 = []
    for doll in dolls:
        name = doll[0]
        count = 0
        idxs = []
        i = len(word)-1
        while i < len(name):
            if name[i] == word[l-1]:
                # print(name[i], word[l-1], name[i-l+1:i+1], word)
                # print("---", ''.join(name[i-l:i]), word)
                if ''.join(name[i-l+1:i+1]) == word:
                    count += 1
                    i += l-1
                    idxs.append(i)
            i += 1
        if count > 0:
            answer2.append((count, idxs, doll[1], doll[2], name))
    
    for a in answer2:
        if a[4] == word:
            answer2.remove(a)
            answer.append(a)
    answer.sort(key=lambda x: [-x[0], x[1], x[2]])
    answer2.sort(key=lambda x: [-x[0], x[1], x[2]])
    answer = answer + answer2

    answer = [x[3] for x in answer]
    if not answer:
        empty_str = "Your search for (" + word + ") didn't return any results"
        answer.append(empty_str)

    return answer


data = ["1 BROWN 0", "2 CONY 0", "3 DOLL 1", "4 DOLL 2",
        "5 LARGE-BROWN 3", "6 SMALL-BROWN 3", "7 BLACK-CONY 4", "8 BROWN-CONY 4"]
word = "BROWN"
data = ["1 ROOTA 0", "2 AA 1", "3 ZZZ 1", "4 AABAA 1", "5 AAAAA 1", "6 AAAA 1", "7 BAAAAAAA 1", "8 BBAA 1", "9 CAA 1", "10 ROOTB 0", "11 AA 10"]
word = "AA"
# solution(data, word)
print(solution(data, word))


["ROOTA/AA","ROOTB/AA","ROOTA/CAA","ROOTA/BBAA","ROOTA/AABAA","ROOTA/AAAA","ROOTA/AAAAA","ROOTA/BAAAAAAA"]
["ROOTA/AA","ROOTB/AA","ROOTA/BAAAAAAA","ROOTA/AAAAA","ROOTA/AAAA","ROOTA/AABAA","ROOTA/CAA","ROOTA/BBAA"]