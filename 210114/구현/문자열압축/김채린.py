def solution(s):
    length = []
    result = ""

    # 길이 1이면 1개 출력
    if len(s) == 1:
        return 1

    #전체 문자열 길이를 2로 나눠서 자른거랑 비교할때 길이 안넘어가게 한다 abcabc dede  => 이런거 방지
    for cut in range(1, len(s) // 2 + 1): 

        # 일단 1부터 세고
        count = 1
         # cut 만큼 잘라서
        cut_str = s[:cut] 

         # i부터..길이까지..cut간격으로 비교! abcabcdede=> cut가3일때 잘라진건abc  그럼 3개단위로 비교 ==abc 몇번 나오나 비교
        for i in range(cut, len(s), cut):

            # 잘라놓은거랑 방금 슬라이싱 한거랑 같으면 카운트(반복횟수) 증가
            if s[i:i+cut] == cut_str:
                count += 1
            # 다르면 카운트(반복횟수)는
            else:
                # 그대로 1일때 반복횟수(카운트) 없애버려
                if count == 1:
                    count = ""

                # 결과값에 반복횟수랑 자른 문자열 붙이고
                result += str(count) + cut_str
                # 다르니까 다음 자른거로 컷스트링 초기화 하고 다시 돌아가서 같은 단위로 다음꺼랑 비교
                cut_str = s[i:i+cut]
                # 카운트도 다시 초기화
                count = 1

        # 제일 마지막에 비교한 문자열이 들어가도록 마지막에 해줘야해
        if count == 1:
            count = ""
        result += str(count) + cut_str
        length.append(len(result))
        print(result)
        # result 초기화
        result = ""
        
        answer=min(length)
        
    return answer


aaa=solution('abcabcdede')
print('답은', aaa)