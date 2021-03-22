def solution(progresses, speeds):
    answer = []
    i = 0
    while i < len(progresses):
        count = (100 - progresses[i]) // speeds[i]
        if (100 - progresses[i]) % speeds[i] != 0:
            count += 1
        for j in range(i, len(progresses)):
            progresses[j] += count * speeds[j]
        count = 0
        while i < len(progresses) and progresses[i] >= 100:
            count += 1
            i += 1
        answer.append(count)

    return answer


progresses = [95, 90, 99, 99, 80, 99]
speeds = [1, 1, 1, 1, 1, 1]
print(solution(progresses, speeds))