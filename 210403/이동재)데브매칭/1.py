def solution(lottos, win_nums):
    answer = []
    count0 = 0
    countWin = 0
    lottos.sort()
    win_nums.sort()

    idx = 0
    for number in lottos:
        if number == 0:
            count0 += 1
        else:
            while idx < 6 and number >= win_nums[idx]:
                if number == win_nums[idx]:
                    countWin += 1
                    break
                else:
                    idx += 1

    mx = 7 - (count0 + countWin)
    if mx > 6:
        mx = 6
    mn = 7 - countWin
    if mn > 6:
        mn = 6
    answer.append(mx)
    answer.append(mn)
    return answer


lottos = [44, 1, 0, 0, 31, 25]
win_nums = [31, 10, 45, 1, 6, 19]
print(solution(lottos, win_nums))