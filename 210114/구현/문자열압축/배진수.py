def solution(s):
    answer = len(s)
    check_size = int(len(s)/2)+1
    for i in range(1,check_size):
        count = 1
        len_check = []
        times = 0
        for j in range(i,len(s),i):
            times += 1
            if  s[j-i:j] == s[j:j+i]:
                count += 1
                if (len(s)-1) // i == times:
                    len_check.append(str(count))
                    len_check.append(s[j:j+i])
                    count = 1
            elif count == 1 and s[j:j+i] != s[j-i:j]:
                len_check.append(s[j-i:j])
                if (len(s)-1) // i == times:
                    len_check.append(s[j:j+i])
            elif count > 1 and s[j:j+i] != s[j-i:j]:
                len_check.append(str(count))
                len_check.append(s[j-i:j])
                count = 1
                if (len(s)-1) // i == times:
                    len_check.append(s[j:j+i])
        res = "".join(len_check)
        answer = min(answer, len(res))
    return answer