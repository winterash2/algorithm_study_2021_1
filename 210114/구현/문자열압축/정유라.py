def solution(s):
    # 초기화
    i = 0           # 인덱스
    m = ""          # 압축할 문자열
    len_m = 1       # 압축할 문자열 단위
    isDiff = True   # 압축할 문자열과 다른지 ex) m = "ab"일 때 "abcd"인 경우 "ab" =/= "cd"
    count = 1       # 몇번 압축됐는지
    total = ""      # 압축 후 최종 문자열

    min_total = ""              # 최소로 압축된 문자열
    min_total_length = 10000    # 최소로 압축된 문자열의 길이



    # aabbaccc 인 경우
    # m단위가 1일 때 => a, b, a, c
    # m단위가 2일 때 => aa, bb, ac, cc
    # m단위가 3일 때 => aab, bac, 
    #     :
    # m단위가 8일 때 => aabbaccc

    # 인덱스를 하나씩 옮겨가면서 압축문자열 직후 인덱스에서 압축문자열이 반복되면 (find로 찾는다) count를 +1 해준다
    # 1. 다음 가리키는 문자열 단위가 압축 문자열 m과 같으면 count를 올리고 다음 인덱스로 넘어간다 
    # 2. 

    while True:
        if isDiff == True:
            if count == 1:
                total += m
            else:
                total += str(count)+m
            count = 1
            m = ""

            # 남은 문자열에서 현재 압축문자열단위(len_m)로 더이상 압축 문자열을 만들 수 없을 때 
            if i+len_m > len(s):
                total += s[i: len(s)]   # 남아있는 문자들을 붙여주고 
                # 최소 압축 문자열인지 확인한다.
                if len(total) < min_total_length:
                    min_total_length = len(total)
                    min_total = total
                
                # 압축문자열 길이 +1
                i = 0
                len_m += 1
                total = ""

                # 입력받은 문자열 전체가 압축할 문자열인 경우 break
                if len_m >= len(s):
                    break
            
            # 압축할 문자열
            for x in range(i, i+len_m):
                m += s[x]
            
            i += len_m      # 인덱스 옮기기
            isDiff = False

        # 현재 인덱스에서부터 m이 나오는지
        if s.find(m, i) == i:
            i += len_m
            count += 1
        else:
            isDiff = True

    print(min_total)
    print("result", min_total_length)
    return min_total_length
solution("xababcdcdababcdcd")