def solution(name):
    count = []
    for i in range(len(name)):
        count.append(min(ord(name[i]) - ord('A'), 91 - ord(name[i])))

    if 0 not in count:
        return (sum(count) + len(count) - 1)
    else:
        idx, answer = 0, 0
        while 1:
            answer += count[idx]
            count[idx] = 0
            if sum(count) == 0:
                break
            left, right = 1, 1
            while count[idx-left] == 0:
                left += 1
            while count[idx+right] == 0:
                right += 1
            if left < right:
                answer += left
                idx -= left
            else:
                answer += right
                idx += right
        return answer